from sqlalchemy.orm import Session
from app.models.mating_request import MatingRequest
from app.schemas.mating_request import MatingRequestCreate, MatingRequestUpdate


def create_mating_request(db: Session, req: MatingRequestCreate) -> MatingRequest:
    db_req = MatingRequest(**req.model_dump())
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req


def get_mating_requests(db: Session, skip=0, limit=10):
    return db.query(MatingRequest).offset(skip).limit(limit).all()


def get_pet_mating_requests(db: Session, pet_id: int):
    return db.query(MatingRequest).filter_by(requester_pet_id=pet_id).all()


def update_mating_status(db: Session, request_id: int, status: str):
    db_req = db.query(MatingRequest).get(request_id)
    if db_req:
        db_req.status = status
        db.commit()
        db.refresh(db_req)
    return db_req