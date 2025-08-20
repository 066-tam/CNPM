
from sqlalchemy.orm import Session
from app.models.recruitment import Campaign, Job, Application
from app.repositories.campaign_repo import CampaignRepository
from app.repositories.job_repo import JobRepository
from app.repositories.application_repo import ApplicationRepository

class RecruitmentService:
    def __init__(self, db: Session):
        self.campaigns = CampaignRepository(db)
        self.jobs = JobRepository(db)
        self.apps = ApplicationRepository(db)

    def create_campaign(self, **data): return self.campaigns.create(Campaign(**data))
    def create_job(self, **data): return self.jobs.create(Job(**data))
    def submit_application(self, **data): return self.apps.create(Application(**data))
