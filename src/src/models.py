from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Intern(db.Model):
    __tablename__ = "interns"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skills = db.Column(db.String(255))

class InternshipCampaign(db.Model):
    __tablename__ = "internship_campaigns"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)

class TrainingProgram(db.Model):
    __tablename__ = "training_programs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    goals = db.Column(db.Text)
