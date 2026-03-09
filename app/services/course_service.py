
from app.repositories.course_repository import CourseRepository
from app.utils.response import success_response

class CourseService:

    def __init__(self, db):
        self.repo = CourseRepository(db)

    def create_course(self, course):
        new_course = self.repo.create(course)
        return success_response(new_course)

    def list_courses(self):
        return success_response(self.repo.get_all())
