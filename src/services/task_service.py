from src.data.models.task import Task
from src.data.repositories.task_repo import TaskRepository


class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, name, description, user_id):
        task = Task(title=name, description=description, user_id=user_id)
        return self.task_repository.save_task(task)

    def get_all_task(self):
        return self.task_repository.get_all_tsks()

    def get_task_by_id(self, task_id):
        return self.task_repository.get_task_by_id(task_id)

    def update_task(self, task_id, updated_data):
        return self.task_repository.update_task(task_id, updated_data)

    def delete_task(self, task_id):
        self.task_repository.delete_task(task_id)
