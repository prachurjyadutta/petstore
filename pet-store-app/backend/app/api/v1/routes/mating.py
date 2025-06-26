from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.mating_request import MatingRequestCreate, MatingRequestOut, MatingRequestUpdate
from app.crud import crud_mating
from app.db.session import get_db
from typing import List

router = APIRouter(prefix="/mating", tags=["Mating"])

@router.post("/requests", response_model=MatingRequestOut)
def create_mating(req: MatingRequestCreate, db: Session = Depends(get_db)):
    return crud_mating.create_mating_request(db, req)

@router.get("/requests", response_model=List[MatingRequestOut])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_mating.get_mating_requests(db, skip, limit)

@router.get("/pets/{pet_id}/requests", response_model=List[MatingRequestOut])
def read_for_pet(pet_id: int, db: Session = Depends(get_db)):
    return crud_mating.get_pet_mating_requests(db, pet_id)

@router.post("/requests/{request_id}/accept", response_model=MatingRequestOut)
def accept(request_id: int, db: Session = Depends(get_db)):
    return crud_mating.update_mating_status(db, request_id, "accepted")

@router.post("/requests/{request_id}/reject", response_model=MatingRequestOut)
def reject(request_id: int, db: Session = Depends(get_db)):
    return crud_mating.update_mating_status(db, request_id, "rejected")
