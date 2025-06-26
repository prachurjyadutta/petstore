from pydantic import BaseModel
from datetime import datetime

class Bill(BaseModel):
    id: int
    pet_id: int
    amount: float
    date_issued: datetime
