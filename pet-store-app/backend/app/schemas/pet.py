from pydantic import BaseModel
from typing import Optional
from datetime import date


class PetBase(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    birth_date: Optional[date] = None


class PetCreate(PetBase):
    owner_id: int


class PetUpdate(PetBase):
    pass


class PetRead(PetBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # For Pydantic v2 to handle SQLAlchemy models
