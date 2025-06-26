from pydantic import BaseModel
from typing import Optional
from datetime import date
from uuid import UUID

class PetBase(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    birth_date: Optional[date] = None


class PetCreate(PetBase):
    owner_id: str


class PetUpdate(PetBase):
    pass

class PetInDBBase(PetBase):
    id: str
    owner_id: str

    model_config = {
        "from_attributes": True
    }

class Pet(PetInDBBase):
    pass

class PetInDB(PetInDBBase):
    pass
class Pet(PetBase):
    id: UUID
    owner_id: str

    class Config:
        from_attributes = True  # For Pydantic v2 to handle SQLAlchemy models
