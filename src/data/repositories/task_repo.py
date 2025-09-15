from src.schemas.extensions import db
from src.data.models.task import Task


class TaskRepository:

    @staticmethod
    def get_all_tasks():
        return Task.query.all()

    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def save_task(task):
        db.session.add(task)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return task

    @staticmethod
    def update_task(task_id, updated_data):
        task = Task.query.get(task_id, updated_data)
        if task:
            for key, value in updated_data.items():
                setattr(task, key, value)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            return task
        return None

    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            db.session.delete(task)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            return True
        return False