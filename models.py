from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(32), nullable=False)  # HR, Admin, Mentor, Intern, Coordinator

class Intern(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    education = db.Column(db.String(128))
    skills = db.Column(db.String(256))
    mentor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    performance_notes = db.Column(db.Text)
