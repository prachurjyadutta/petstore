from pydantic import BaseModel
from datetime import datetime

class MedicalRecordCreate(BaseModel):
    pet_id: int
    vet_id: int
    date: datetime
    notes: str

class MedicalRecord(MedicalRecordCreate):
    id: int
