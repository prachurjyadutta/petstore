from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class MatingStatus(str, enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class MatingRequest(Base):
    __tablename__ = "mating_requests"

    id = Column(Integer, primary_key=True, index=True)
    requester_pet_id = Column(Integer, ForeignKey("pets.id"), nullable=False)
    desired_breed = Column(String, nullable=False)
    location = Column(String, nullable=True)
    preferred_date_1 = Column(Date)
    preferred_date_2 = Column(Date)
    notes = Column(Text)
    status = Column(Enum(MatingStatus), default=MatingStatus.pending)

    requester_pet = relationship("Pet", back_populates="mating_requests_sent")