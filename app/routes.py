from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlmodel import select
from .db import get_session, init_db
from . import crud, auth, models, schemas

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/token')

def get_current_user(token: str = Depends(oauth2_scheme), session = Depends(get_session)):
    payload = auth.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Invalid token')
    email = payload.get('sub')
    user = crud.get_user_by_email(session, email)
    if not user:
        raise HTTPException(status_code=401, detail='User not found')
    return user

def role_required(roles: list[str]):
    def dep(current_user = Depends(get_current_user)):
        if current_user.role not in roles:
            raise HTTPException(status_code=403, detail='Insufficient role')
        return current_user
    return dep

# AUTH
@router.post('/token', response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), session = Depends(get_session)):
    user = crud.get_user_by_email(session, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Incorrect username or password')
    token = auth.create_access_token(subject=user.email, role=user.role)
    return {'access_token': token, 'token_type': 'bearer'}

# USERS
@router.post('/users', response_model=schemas.UserRead)
def create_user(payload: schemas.UserCreate, session = Depends(get_session)):
    existing = crud.get_user_by_email(session, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail='Email already registered')
    user = crud.create_user(session, payload.email, payload.password, payload.full_name, payload.role)
    return user

# INTERNSHIPS
@router.post('/internships', response_model=schemas.InternshipRead, dependencies=[Depends(role_required(['hr','admin','coordinator']))])
def create_internship(payload: schemas.InternshipCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    data = payload.dict()
    data['created_by'] = current_user.id
    internship = crud.create_internship(session, **data)
    return internship

@router.get('/internships', response_model=list[schemas.InternshipRead])
def list_internships(session = Depends(get_session)):
    return crud.list_internships(session)

# PROFILES
@router.post('/profiles', response_model=schemas.InternProfileRead, dependencies=[Depends(role_required(['intern','hr','admin']))])
def create_profile(payload: schemas.InternProfileCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    if current_user.role == 'intern' and current_user.id != payload.user_id:
        raise HTTPException(status_code=403, detail='Cannot create profile for another user')
    existing = crud.get_profile_by_user(session, payload.user_id)
    if existing:
        raise HTTPException(status_code=400, detail='Profile already exists')
    profile = crud.create_profile(session, **payload.dict())
    return profile

@router.get('/profiles/me', response_model=schemas.InternProfileRead)
def read_my_profile(current_user = Depends(role_required(['intern','hr','admin','mentor'])), session = Depends(get_session)):
    profile = crud.get_profile_by_user(session, current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail='Profile not found')
    return profile

@router.put('/profiles/{profile_id}', response_model=schemas.InternProfileRead, dependencies=[Depends(role_required(['intern','hr','admin']))])
def update_profile(profile_id: int, payload: schemas.InternProfileCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    profile = crud.get_profile(session, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail='Profile not found')
    if current_user.role == 'intern' and profile.user_id != current_user.id:
        raise HTTPException(status_code=403, detail='Cannot edit other profile')
    updated = crud.update_profile(session, profile, **payload.dict())
    return updated

# APPLICATIONS
@router.post('/applications', response_model=schemas.ApplicationRead, dependencies=[Depends(role_required(['intern']))])
def apply(payload: schemas.ApplicationCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    internship = crud.get_internship(session, payload.internship_id)
    if not internship:
        raise HTTPException(status_code=404, detail='Internship not found')
    app = crud.create_application(session, internship_id=payload.internship_id, user_id=current_user.id)
    return app

@router.get('/applications', response_model=list[schemas.ApplicationRead], dependencies=[Depends(role_required(['hr','admin','mentor']))])
def list_applications(session = Depends(get_session)):
    return crud.list_applications(session)

@router.get('/applications/me', response_model=list[schemas.ApplicationRead], dependencies=[Depends(role_required(['intern']))])
def my_applications(current_user = Depends(get_current_user), session = Depends(get_session)):
    return crud.list_applications_for_intern(session, current_user.id)

@router.patch('/applications/{app_id}/status', response_model=schemas.ApplicationRead, dependencies=[Depends(role_required(['hr','admin','coordinator']))])
def change_application_status(app_id: int, status: str = Body(...), session = Depends(get_session)):
    application = crud.get_application(session, app_id)
    if not application:
        raise HTTPException(status_code=404, detail='Application not found')
    updated = crud.update_application_status(session, application, status)
    return updated

# TRAININGS
@router.post('/trainings', response_model=schemas.TrainingRead, dependencies=[Depends(role_required(['coordinator','hr','admin']))])
def create_training(payload: schemas.TrainingCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    data = payload.dict()
    data['coordinator_id'] = current_user.id
    t = crud.create_training(session, **data)
    return t

@router.get('/trainings', response_model=list[schemas.TrainingRead])
def list_trainings(session = Depends(get_session)):
    return crud.list_training(session)

# TASKS
@router.post('/tasks', response_model=schemas.TaskRead, dependencies=[Depends(role_required(['mentor','coordinator']))])
def create_task(payload: schemas.TaskCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    data = payload.dict()
    data['mentor_id'] = current_user.id
    task = crud.create_task(session, **data)
    return task

@router.get('/tasks/me', response_model=list[schemas.TaskRead], dependencies=[Depends(role_required(['intern']))])
def my_tasks(current_user = Depends(get_current_user), session = Depends(get_session)):
    return crud.list_tasks_for_intern(session, current_user.id)

@router.patch('/tasks/{task_id}', response_model=schemas.TaskRead)
def update_task(task_id: int, payload: schemas.TaskCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    task = crud.get_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    if current_user.role not in ['admin','hr'] and task.mentor_id != current_user.id:
        raise HTTPException(status_code=403, detail='Not allowed')
    updated = crud.update_task(session, task, **payload.dict())
    return updated

# FEEDBACK
@router.post('/feedback', response_model=schemas.FeedbackRead)
def create_feedback(payload: schemas.FeedbackCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    data = payload.dict()
    data['from_user_id'] = current_user.id
    f = crud.create_feedback(session, **data)
    return f

@router.get('/feedback/me', response_model=list[schemas.FeedbackRead])
def my_feedback(current_user = Depends(get_current_user), session = Depends(get_session)):
    return crud.list_feedback_for_user(session, current_user.id)

# PERFORMANCE
@router.post('/performance', response_model=schemas.PerformanceRead, dependencies=[Depends(role_required(['mentor','hr','admin']))])
def record_performance(payload: schemas.PerformanceCreate, current_user = Depends(get_current_user), session = Depends(get_session)):
    data = payload.dict()
    data['mentor_id'] = current_user.id
    p = crud.create_performance(session, **data)
    return p

@router.get('/performance/me', response_model=list[schemas.PerformanceRead], dependencies=[Depends(role_required(['intern']))])
def my_performance(current_user = Depends(get_current_user), session = Depends(get_session)):
    return crud.list_performance_for_intern(session, current_user.id)

# App
from fastapi import FastAPI
app = FastAPI(title='IMS API - Complete')

@app.on_event('startup')
def on_startup():
    init_db()

app.include_router(router, prefix='/api')

@app.get('/')
def root():
    return {'status': 'IMS API running'}
