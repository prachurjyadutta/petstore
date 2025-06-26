from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import User, UserCreate
from app.crud import crud_user
from app.db.session import get_db
from app.schemas import pet as pet_schema
from app.crud import crud_pet
from uuid import UUID


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)

@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/pets", response_model=List[pet_schema.Pet])
def get_user_pets(user_id: UUID, db: Session = Depends(get_db)):
    pets = crud_pet.get_pets_by_user(db, user_id)
    # Avoid checking "is None" – instead check if it's empty
    if not pets:
        raise HTTPException(status_code=404, detail="User not found or has no pets")
    return pets
