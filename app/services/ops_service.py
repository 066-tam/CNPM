
from sqlalchemy.orm import Session
from app.models.ops import Interview, DailyLog, KPI, Assessment, Feedback, Message
from app.repositories.interview_repo import InterviewRepository
from app.repositories.daily_log_repo import DailyLogRepository
from app.repositories.kpi_repo import KPIRepository
from app.repositories.assessment_repo import AssessmentRepository
from app.repositories.feedback_repo import FeedbackRepository
from app.repositories.message_repo import MessageRepository

class OpsService:
    def __init__(self, db: Session):
        self.interviews = InterviewRepository(db)
        self.logs = DailyLogRepository(db)
        self.kpis = KPIRepository(db)
        self.assessments = AssessmentRepository(db)
        self.feedbacks = FeedbackRepository(db)
        self.messages = MessageRepository(db)

    def schedule_interview(self, **data): return self.interviews.create(Interview(**data))
    def log_daily(self, **data): return self.logs.create(DailyLog(**data))
    def set_kpi(self, **data): return self.kpis.create(KPI(**data))
    def assess(self, **data): return self.assessments.create(Assessment(**data))
    def send_feedback(self, **data): return self.feedbacks.create(Feedback(**data))
    def send_message(self, **data): return self.messages.create(Message(**data))
    def inbox(self, user_id: int): return [m for m in self.messages.list() if m.receiver_id == user_id]
