from sqlalchemy.orm import Session
from app.models.training import TrainingProgram
from typing import Iterable, Optional

class TrainingProgramRepository:
    def __init__(self, db: Session): self.db = db
    def list(self) -> Iterable[TrainingProgram]: return self.db.query(TrainingProgram).all()
    def get(self, _id: int) -> Optional[TrainingProgram]: return self.db.get(TrainingProgram, _id)
    def create(self, obj: TrainingProgram) -> TrainingProgram:
        self.db.add(obj); self.db.flush(); return obj
    def update(self, _id: int, **data) -> TrainingProgram:
        obj = self.get(_id); 
        for k,v in data.items(): setattr(obj, k, v)
        self.db.flush(); return obj
    def delete(self, _id: int) -> None:
        obj = self.get(_id); 
        if obj: self.db.delete(obj)