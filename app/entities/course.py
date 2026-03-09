
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    workload = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="course")
