from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.db.init_db import init_db
from app.db.session import engine
from app.db.base_class import Base

from app.api.v1.routes import (
    auth,
    users,
    pets,
    adoptions,
    reviews,
    appointments_extra,
    appointments,
    bills,
    inventory,
    mating,
    medical_records,
    medications,
    notifications,
    orders,
    payments,
    reports,
    vets,
)

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Pet Store API",
    description="API for managing pet store operations.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    init_db()

origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://127.0.0.1:3000",
]
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1", tags=["Users"])
app.include_router(pets.router, prefix="/api/v1", tags=["Pets"])
app.include_router(adoptions.router)
app.include_router(reviews.router)
app.include_router(appointments_extra.router)
app.include_router(appointments.router)
app.include_router(bills.router)
app.include_router(inventory.router)
app.include_router(mating.router)
app.include_router(medical_records.router)
app.include_router(medications.router)
app.include_router(notifications.router)
app.include_router(orders.router)
app.include_router(payments.router)
app.include_router(reports.router)
app.include_router(vets.router)