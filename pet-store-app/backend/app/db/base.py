# app/db/base.py

from app.db.base_class import Base

# Explicit imports to register models with Base metadata
from app.models.user import User
from app.models.pet import Pet
from app.models.vet import Vet
from app.models.appointment import Appointment
from app.models.bill import Bill
from app.models.inventory import InventoryItem
from app.models.mating_request import MatingRequest
from app.models.medical_record import MedicalRecord
from app.models.medication import Medication
