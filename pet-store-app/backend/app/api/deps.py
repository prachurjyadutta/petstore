from typing import Generator
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

# Dependency to get DB session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
