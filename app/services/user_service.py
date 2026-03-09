
from app.repositories.user_repository import UserRepository
from app.utils.response import success_response, error_response

class UserService:

    def __init__(self, db):
        self.repo = UserRepository(db)

    def create_user(self, user):

        if self.repo.get_by_email(user.email):
            return error_response("Email already exists")

        new_user = self.repo.create(user)

        return success_response(new_user, "User created")

    def list_users(self):
        users = self.repo.get_all()
        return success_response(users)
