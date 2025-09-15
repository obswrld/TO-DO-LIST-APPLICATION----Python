from data.models.user import User
from src.data.repositories import user_repositories


class UserService:

    def __init__(self):
        self.user_repository = user_repositories.UserRepository()


    def create_user(self, username, email, password):
        user = User(username, email, password)
        return self.user_repository.save_user(user)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def update_user(self, user_id,updated_data):
        return self.user_repository.update_user(user_id, updated_data)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)