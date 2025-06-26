from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
import uuid

def create_user(db: Session, user: UserCreate):
    db_user = User(id=str(uuid.uuid4()), **user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
    return db.query(User).all()