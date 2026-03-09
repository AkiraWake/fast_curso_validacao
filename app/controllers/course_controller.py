
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal
from app.services.course_service import CourseService
from app.schemas.course_schema import CourseCreate

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return CourseService(db).create_course(course)

@router.get("/")
def list_courses(db: Session = Depends(get_db)):
    return CourseService(db).list_courses()
