from pydantic import BaseModel

class InventoryItem(BaseModel):
    id: int
    name: str
    quantity: int
