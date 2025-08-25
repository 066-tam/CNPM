from sqlmodel import Session
from .db import engine, init_db
from . import crud

def create_sample():
    init_db()
    with Session(engine) as session:
        users = [
            ('admin@example.com','password','Admin','admin'),
            ('hr@example.com','password','HR','hr'),
            ('coord@example.com','password','Coordinator','coordinator'),
            ('mentor@example.com','password','Mentor','mentor'),
            ('intern@example.com','password','Intern','intern'),
        ]
        for email, pw, name, role in users:
            existing = crud.get_user_by_email(session, email)
            if not existing:
                crud.create_user(session, email, pw, name, role)
        # create internship
        existing_internships = crud.list_internships(session)
        if not existing_internships:
            crud.create_internship(session, title='Backend Intern', description='Work on APIs', location='HCMC')

if __name__ == '__main__':
    create_sample()
    print('Sample data created')