from fastapi import APIRouter
from typing import List
from app.models.medical_record import MedicalRecord
from app.schemas.medical_record import MedicalRecordCreate

router = APIRouter(prefix="/medical-records", tags=["Medical Records"])

records_db: List[MedicalRecord] = []

@router.get("/", response_model=List[MedicalRecord])
def list_records():
    return records_db

@router.post("/", response_model=MedicalRecord)
def create_record(record: MedicalRecordCreate):
    new_record = MedicalRecord(id=len(records_db) + 1, **record.dict())
    records_db.append(new_record)
    return new_record
