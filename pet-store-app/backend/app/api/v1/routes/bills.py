from fastapi import APIRouter
from typing import List
from app.models.bill import Bill
from app.schemas.bill import BillCreate

router = APIRouter(prefix="/bills", tags=["Bills"])
bills_db: List[Bill] = []

@router.get("/", response_model=List[Bill])
def list_bills():
    return bills_db

@router.post("/", response_model=Bill)
def create_bill(bill: BillCreate):
    new_bill = Bill(id=len(bills_db) + 1, **bill.dict())
    bills_db.append(new_bill)
    return new_bill
