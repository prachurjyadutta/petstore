from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.pet import PetRead  # ✅ Use schema for response
from app.models.pet import Pet
from app.db.session import get_db

router = APIRouter(prefix="/pets", tags=["Pets"])


@router.get("/", response_model=List[PetRead])
def get_pets(db: Session = Depends(get_db)):
    pets = db.query(Pet).all()
    return pets
