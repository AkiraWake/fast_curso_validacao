
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database import SessionLocal
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)

@router.get("/")
def list_users(db: Session = Depends(get_db)):
    return UserService(db).list_users()
