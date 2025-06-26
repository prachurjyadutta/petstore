from pydantic import BaseModel
from datetime import datetime

class BillCreate(BaseModel):
    pet_id: int
    amount: float
    date_issued: datetime

class Bill(BillCreate):
    id: int
