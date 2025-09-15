from src.data.models.user import User
from src.data.repositories.user_repositories import UserRepository
from werkzeug.security import generate_password_hash

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()


    def create_user(self, username, email, password):
        hashed_password = generate_password_hash(password)
        user = User(username, email, hashed_password)
        return self.user_repository.save_user(user)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def update_user(self, user_id,updated_data):
        return self.user_repository.update_user(user_id, updated_data)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

    def get_task_by_id(self, task_id):
        task = self.task_repo.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        return task