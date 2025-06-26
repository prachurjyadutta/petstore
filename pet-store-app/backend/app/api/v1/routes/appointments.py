from fastapi import APIRouter, HTTPException
from typing import List
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate

router = APIRouter(prefix="/appointments", tags=["Appointments"])

appointments_db: List[Appointment] = []

@router.get("/", response_model=List[Appointment])
def list_appointments():
    return appointments_db

@router.post("/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate):
    new_appt = Appointment(id=len(appointments_db) + 1, **appointment.dict())
    appointments_db.append(new_appt)
    return new_appt
