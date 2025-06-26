from pydantic import BaseModel

class Medication(BaseModel):
    id: int
    name: str
    dosage: str
