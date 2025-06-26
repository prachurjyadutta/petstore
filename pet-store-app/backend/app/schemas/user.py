from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False


class User(UserBase):
    id: UUID
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True  # For Pydantic v2 to support ORM models
