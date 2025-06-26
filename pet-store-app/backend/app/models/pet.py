from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import uuid

class Pet(Base):
    __tablename__ = "pets"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)
    owner_id = Column(String, ForeignKey("users.id"))

    mating_requests_sent = relationship("MatingRequest", back_populates="requester_pet")
    owner = relationship("User", back_populates="pets")  # ✅ Matches above
