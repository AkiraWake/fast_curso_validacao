
from fastapi import FastAPI
from app.infrastructure.database import engine, Base

from app.controllers import user_controller
from app.controllers import course_controller
from app.controllers import enrollment_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Courses API")

app.include_router(user_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)
