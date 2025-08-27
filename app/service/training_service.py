from sqlalchemy.orm import Session
from app.models.training import TrainingProgram, Course, Enrollment
from app.repositories.program_repo import TrainingProgramRepository
from app.repositories.course_repo import CourseRepository
from app.repositories.enrollment_repo import EnrollmentRepository

class TrainingService:
    def __init__(self, db: Session):
        self.programs = TrainingProgramRepository(db)
        self.courses = CourseRepository(db)
        self.enrollments = EnrollmentRepository(db)

    def create_program(self, **data): return self.programs.create(TrainingProgram(**data))
    def create_course(self, **data): return self.courses.create(Course(**data))
    def enroll(self, course_id: int, user_id: int):
        return self.enrollments.create(Enrollment(course_id=course_id, user_id=user_id))
