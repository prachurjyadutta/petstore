from pydantic import BaseModel

class InventoryItemCreate(BaseModel):
    name: str
    quantity: int

class InventoryItem(InventoryItemCreate):
    id: int
