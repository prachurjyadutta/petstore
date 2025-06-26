from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/payments", tags=["Payments"])

class Payment(BaseModel):
    id: int
    order_id: int
    user_id: int
    amount: float
    method: str
    created_at: datetime

@router.post("/", response_model=Payment)
def record_payment(payment: Payment):
    return payment
