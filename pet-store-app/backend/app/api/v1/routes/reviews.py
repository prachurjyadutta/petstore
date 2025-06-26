from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/reviews", tags=["Reviews"])

class Review(BaseModel):
    id: int
    vet_id: int
    user_id: int
    rating: int
    comment: str

@router.post("/", response_model=Review)
def leave_review(review: Review):
    return review

@router.get("/{vet_id}", response_model=List[Review])
def get_reviews(vet_id: int):
    return []
