from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    pet_id: int
    appointment_time: datetime
    reason: str

class Appointment(AppointmentCreate):
    id: int
