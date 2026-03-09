
from app.entities.enrollment import Enrollment

class EnrollmentRepository:

    def __init__(self, db):
        self.db = db

    def create(self, enrollment):
        new_enrollment = Enrollment(**enrollment.dict())
        self.db.add(new_enrollment)
        self.db.commit()
        self.db.refresh(new_enrollment)
        return new_enrollment

    def get_existing(self, user_id, course_id):
        return self.db.query(Enrollment).filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id
        ).first()
