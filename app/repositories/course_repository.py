
from app.entities.course import Course

class CourseRepository:

    def __init__(self, db):
        self.db = db

    def create(self, course):
        new_course = Course(**course.dict())
        self.db.add(new_course)
        self.db.commit()
        self.db.refresh(new_course)
        return new_course

    def get_all(self):
        return self.db.query(Course).all()

    def get_by_id(self, course_id):
        return self.db.query(Course).filter(Course.id == course_id).first()
