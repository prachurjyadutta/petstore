# app/db/init_db.py
from app.db.session import engine
from app.db.base_class import Base

# Import all models here to register them with SQLAlchemy
from app.models import user, pet, vet, appointment, bill, inventory, mating_request, medical_record, medication

def init_db():
    Base.metadata.create_all(bind=engine)
