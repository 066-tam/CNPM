from sqlalchemy.orm import Session
from app.models.recruitment import Campaign
from typing import Iterable, Optional

class CampaignRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[Campaign]: return self.db.query(Campaign).all()
    def get(self, _id: int) -> Optional[Campaign]: return self.db.get(Campaign, _id)
    def create(self, obj: Campaign) -> Campaign:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> Campaign:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)