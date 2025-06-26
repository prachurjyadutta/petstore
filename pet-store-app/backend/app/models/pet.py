from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    breed = Column(String, nullable=True)
    birth_date = Column(Date, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    mating_requests_sent = relationship("MatingRequest", back_populates="requester_pet")
