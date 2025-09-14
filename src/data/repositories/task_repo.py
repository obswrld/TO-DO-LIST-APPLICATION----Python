from src.schemas import db
from src.data.models.task import Task

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get(task_id)

def save_task(task):
    db.session.add(task)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return task

def update_task(task, updated_data):
    task = get_task_by_id(task.id)
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

def delete_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        db.session.delete(task)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return True
    return False