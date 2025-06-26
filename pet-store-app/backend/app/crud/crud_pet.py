from sqlalchemy.orm import Session
from app.models.pet import Pet
from app.schemas.pet import PetCreate, PetUpdate
from typing import List
from app import models
from uuid import UUID

def get_pet(db: Session, pet_id: int):
    return db.query(Pet).filter(Pet.id == pet_id).first()

def get_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pet).offset(skip).limit(limit).all()

def create_pet(db: Session, pet: PetCreate):
    db_pet = Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def update_pet(db: Session, db_pet: Pet, updates: PetUpdate):
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(db_pet, key, value)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def delete_pet(db: Session, db_pet: Pet):
    db.delete(db_pet)
    db.commit()
    return db_pet


def get_pets_by_user(db: Session, user_id: UUID) -> List[Pet]:
    return db.query(Pet).filter(Pet.owner_id == str(user_id)).all()
