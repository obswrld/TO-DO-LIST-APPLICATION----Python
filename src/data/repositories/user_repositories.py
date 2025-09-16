from src.schemas.extensions import db
from src.data.models.user import User

class UserRepository:

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def save_user(user):
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return user

    @staticmethod
    def update_user(user_id, updated_data):
        user = User.query.get(user_id)
        if user:
            for key, value in updated_data.items():
                setattr(user, key, value)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            return True
        return False