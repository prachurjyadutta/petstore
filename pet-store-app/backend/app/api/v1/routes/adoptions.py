from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/pet-adoptions", tags=["Pet Adoptions"])

class AdoptionRequest(BaseModel):
    id: int
    pet_id: int
    user_id: int
    status: str  # pending, approved, rejected

@router.post("/", response_model=AdoptionRequest)
def create_adoption(request: AdoptionRequest):
    return request

@router.get("/", response_model=List[AdoptionRequest])
def list_adoptions():
    return []
