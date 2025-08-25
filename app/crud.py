from sqlmodel import select
from .models import User, Internship, InternProfile, Application, TrainingProgram, Task, Feedback, PerformanceEntry
from .auth import get_password_hash

# Users
def create_user(session, email: str, password: str, full_name: str | None, role: str) -> User:
    user = User(email=email, full_name=full_name, hashed_password=get_password_hash(password), role=role)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_email(session, email: str):
    return session.exec(select(User).where(User.email == email)).first()

def get_user(session, user_id: int):
    return session.get(User, user_id)

# Internships
def create_internship(session, **data) -> Internship:
    internship = Internship(**data)
    session.add(internship)
    session.commit()
    session.refresh(internship)
    return internship

def list_internships(session):
    return session.exec(select(Internship)).all()

def get_internship(session, internship_id: int):
    return session.get(Internship, internship_id)

# Profiles
def create_profile(session, **data) -> InternProfile:
    profile = InternProfile(**data)
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile

def get_profile_by_user(session, user_id: int):
    return session.exec(select(InternProfile).where(InternProfile.user_id == user_id)).first()

def get_profile(session, profile_id: int):
    return session.get(InternProfile, profile_id)

def update_profile(session, profile: InternProfile, **data):
    for k, v in data.items():
        setattr(profile, k, v)
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return profile

# Applications
def create_application(session, **data) -> Application:
    app = Application(**data)
    session.add(app)
    session.commit()
    session.refresh(app)
    return app

def get_application(session, app_id: int):
    return session.get(Application, app_id)

def list_applications_for_intern(session, user_id: int):
    return session.exec(select(Application).where(Application.user_id == user_id)).all()

def list_applications(session):
    return session.exec(select(Application)).all()

def update_application_status(session, application: Application, status: str):
    application.status = status
    session.add(application)
    session.commit()
    session.refresh(application)
    return application

# Trainings
def create_training(session, **data) -> TrainingProgram:
    t = TrainingProgram(**data)
    session.add(t)
    session.commit()
    session.refresh(t)
    return t

def list_training(session):
    return session.exec(select(TrainingProgram)).all()

# Tasks
def create_task(session, **data) -> Task:
    t = Task(**data)
    session.add(t)
    session.commit()
    session.refresh(t)
    return t

def get_task(session, task_id: int):
    return session.get(Task, task_id)

def list_tasks_for_intern(session, user_id: int):
    return session.exec(select(Task).where(Task.assigned_to == user_id)).all()

def update_task(session, task: Task, **data):
    for k, v in data.items():
        setattr(task, k, v)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# Feedback
def create_feedback(session, **data) -> Feedback:
    f = Feedback(**data)
    session.add(f)
    session.commit()
    session.refresh(f)
    return f

def list_feedback_for_user(session, user_id: int):
    return session.exec(select(Feedback).where(Feedback.to_user_id == user_id)).all()

# Performance
def create_performance(session, **data) -> PerformanceEntry:
    p = PerformanceEntry(**data)
    session.add(p)
    session.commit()
    session.refresh(p)
    return p

def list_performance_for_intern(session, intern_id: int):
    return session.exec(select(PerformanceEntry).where(PerformanceEntry.intern_id == intern_id)).all()
