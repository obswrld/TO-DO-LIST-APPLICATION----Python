from data.models.label import Label
from src.schemas import db


def get_or_create_label(label_name):
    label_instance = Label.query.filter_by(name=label_name).first()
    if not label_instance:
        label_instance = Label(name=label_name)
        db.session.add(label_instance)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    return label_instance

def get_all_labels():
    return Label.query.all()

def update_label(label_id, updated_data):
    label_instance = get_or_create_label(label_id)
    if label_instance:
        for key, value in updated_data.items():
            setattr(label_instance, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return label_instance
    return None

def delete_label(label_id):
    label_instance = get_or_create_label(label_id)
    if label_instance:
        db.session.delete(label_instance)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        return True
    return False