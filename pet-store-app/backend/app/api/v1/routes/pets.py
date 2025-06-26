from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import pet as pet_schema
from app.crud import crud_pet
from app.api import deps

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("/", response_model=pet_schema.Pet)
def create_pet(pet: pet_schema.PetCreate, db: Session = Depends(deps.get_db)):
    return crud_pet.create_pet(db, pet)

@router.get("/", response_model=list[pet_schema.Pet])
def read_pets(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return crud_pet.get_pets(db, skip=skip, limit=limit)

@router.get("/{pet_id}", response_model=pet_schema.Pet)
def read_pet(pet_id: int, db: Session = Depends(deps.get_db)):
    db_pet = crud_pet.get_pet(db, pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet

@router.put("/{pet_id}", response_model=pet_schema.Pet)
def update_pet(pet_id: int, pet: pet_schema.PetUpdate, db: Session = Depends(deps.get_db)):
    db_pet = crud_pet.get_pet(db, pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return crud_pet.update_pet(db, db_pet, pet)

@router.delete("/{pet_id}", response_model=pet_schema.Pet)
def delete_pet(pet_id: int, db: Session = Depends(deps.get_db)):
    db_pet = crud_pet.get_pet(db, pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return crud_pet.delete_pet(db, db_pet)
