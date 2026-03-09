
from app.entities.user import User

class UserRepository:

    def __init__(self, db):
        self.db = db

    def create(self, user):
        new_user = User(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_all(self):
        return self.db.query(User).all()

    def get_by_id(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def delete(self, user):
        self.db.delete(user)
        self.db.commit()
