
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.user_repository import UserRepository
from app.repositories.course_repository import CourseRepository
from app.utils.response import success_response, error_response

class EnrollmentService:

    def __init__(self, db):
        self.repo = EnrollmentRepository(db)
        self.user_repo = UserRepository(db)
        self.course_repo = CourseRepository(db)

    def create_enrollment(self, enrollment):

        user = self.user_repo.get_by_id(enrollment.user_id)
        if not user:
            return error_response("User not found")

        course = self.course_repo.get_by_id(enrollment.course_id)
        if not course:
            return error_response("Course not found")

        existing = self.repo.get_existing(enrollment.user_id, enrollment.course_id)

        if existing:
            return error_response("User already enrolled in this course")

        new_enrollment = self.repo.create(enrollment)

        return success_response(new_enrollment, "Enrollment created")
