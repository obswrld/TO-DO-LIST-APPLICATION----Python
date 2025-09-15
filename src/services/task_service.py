from data.models.task import Task
from src.data.repositories import task_repo

class TaskService:
    def __init__(self):
        self.task_repository = task_repo()

    def create_task(self, name, description):
        task = Task(title=name, description=description)
        return self.task_repository.save_task(task)

    def get_all_task(self):
        return self.task_repository.get_all_tsks()

    def get_task_by_id(self, id):
        return self.task_repository.get_task_by_id(id)

    def update_task(self, id, title, description):
        self.task_repository.update_task(id, title, description)

    def delete_task(self, id):
        self.task_repository.delete_task(id)
