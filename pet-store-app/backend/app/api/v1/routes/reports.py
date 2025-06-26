from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/daily-appointments")
def daily_appointments():
    return {"appointments": 5}

@router.get("/revenue")
def revenue():
    return {"revenue": 1000.0}

@router.get("/inventory-status")
def inventory_status():
    return {"items_low": ["Dog food", "Cat litter"]}
