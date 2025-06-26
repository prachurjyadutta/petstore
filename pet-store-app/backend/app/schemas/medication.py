from pydantic import BaseModel

class MedicationCreate(BaseModel):
    name: str
    dosage: str

class Medication(MedicationCreate):
    id: int
