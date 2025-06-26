from fastapi import APIRouter
from typing import List
from app.models.inventory import InventoryItem
from app.schemas.inventory import InventoryItemCreate

router = APIRouter(prefix="/inventory", tags=["Inventory"])

inventory_db: List[InventoryItem] = []

@router.get("/", response_model=List[InventoryItem])
def list_inventory():
    return inventory_db

@router.post("/", response_model=InventoryItem)
def create_inventory_item(item: InventoryItemCreate):
    new_item = InventoryItem(id=len(inventory_db) + 1, **item.dict())
    inventory_db.append(new_item)
    return new_item
