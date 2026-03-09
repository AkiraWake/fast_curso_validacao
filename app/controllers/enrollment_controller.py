
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal
from app.services.enrollment_service import EnrollmentService
from app.schemas.enrollment_schema import EnrollmentCreate

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    return EnrollmentService(db).create_enrollment(enrollment)
