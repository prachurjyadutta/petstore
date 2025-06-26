from fastapi import APIRouter
from typing import List
from app.models.medication import Medication
from app.schemas.medication import MedicationCreate

router = APIRouter(prefix="/medications", tags=["Medications"])

med_db: List[Medication] = []

@router.get("/", response_model=List[Medication])
def list_medications():
    return med_db

@router.post("/", response_model=Medication)
def create_medication(med: MedicationCreate):
    new_med = Medication(id=len(med_db) + 1, **med.dict())
    med_db.append(new_med)
    return new_med
