from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.db.base_class import Base
from app.db.session import engine


# app/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class User(Base):
    __tablename__ = "users"  # ✅ REQUIRED

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Integer, default=1)