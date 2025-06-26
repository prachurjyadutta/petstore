from pydantic import BaseModel
from datetime import datetime

class MedicalRecord(BaseModel):
    id: int
    pet_id: int
    vet_id: int
    date: datetime
    notes: str
