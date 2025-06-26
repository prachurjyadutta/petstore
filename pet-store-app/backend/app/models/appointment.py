from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Appointment(BaseModel):
    id: int
    pet_id: int
    appointment_date: datetime
    reason: Optional[str]
    notes: Optional[str]
