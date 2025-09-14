from schemas import db
from src.data.models.user import User

class UserRepository(User):

    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()

    def save_user(self, user):
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return user

    def update_user(self, user_id, updated_data):
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

    def delete_user(self, user_id):
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