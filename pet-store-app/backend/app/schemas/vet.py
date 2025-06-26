from pydantic import BaseModel

class VetCreate(BaseModel):
    name: str
    specialization: str

class Vet(VetCreate):
    id: int
