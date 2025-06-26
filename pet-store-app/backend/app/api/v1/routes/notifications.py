from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/notifications", tags=["Notifications"])

class Notification(BaseModel):
    id: int
    user_id: int
    message: str
    read: bool

@router.get("/", response_model=List[Notification])
def get_notifications():
    return []

@router.post("/", response_model=Notification)
def send_notification(notification: Notification):
    return notification

@router.patch("/{id}/read")
def mark_as_read(id: int):
    return {"id": id, "read": True}
