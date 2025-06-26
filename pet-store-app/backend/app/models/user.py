from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base
from sqlalchemy.orm import relationship
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    # Add to the User model
    pets = relationship("Pet", back_populates="owner")
    