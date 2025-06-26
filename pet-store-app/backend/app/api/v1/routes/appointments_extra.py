from fastapi import APIRouter

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/{appointment_id}/confirm")
def confirm_appointment(appointment_id: int):
    return {"appointment_id": appointment_id, "status": "confirmed"}

@router.post("/{appointment_id}/cancel")
def cancel_appointment(appointment_id: int):
    return {"appointment_id": appointment_id, "status": "cancelled"}

@router.post("/{appointment_id}/reschedule")
def reschedule_appointment(appointment_id: int):
    return {"appointment_id": appointment_id, "status": "rescheduled"}
