from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/orders", tags=["Orders"])

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    id: int
    user_id: int
    items: List[OrderItem]
    total_amount: float
    status: str  # pending, paid, cancelled
    created_at: datetime

@router.get("/", response_model=List[Order])
def get_orders():
    return []

@router.post("/", response_model=Order)
def create_order(order: Order):
    return order
