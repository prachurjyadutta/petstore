from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

class MatingRequestBase(BaseModel):
    requester_pet_id: int
    desired_breed: str
    location: Optional[str]
    preferred_date_1: Optional[date]
    preferred_date_2: Optional[date]
    notes: Optional[str]

class MatingRequestCreate(MatingRequestBase):
    pass

class MatingRequestUpdate(BaseModel):
    status: Literal["accepted", "rejected"]

class MatingRequestOut(MatingRequestBase):
    id: int
    status: str

    class Config:
        from_attributes = True