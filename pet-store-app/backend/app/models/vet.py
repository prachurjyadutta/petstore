from pydantic import BaseModel

class Vet(BaseModel):
    id: int
    name: str
    specialization: str
