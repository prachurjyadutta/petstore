from fastapi import APIRouter
from typing import List
from app.models.vet import Vet
from app.schemas.vet import VetCreate

router = APIRouter(prefix="/vets", tags=["Vets"])

vets_db: List[Vet] = []

@router.get("/", response_model=List[Vet])
def list_vets():
    return vets_db

@router.post("/", response_model=Vet)
def create_vet(vet: VetCreate):
    new_vet = Vet(id=len(vets_db) + 1, **vet.dict())
    vets_db.append(new_vet)
    return new_vet
