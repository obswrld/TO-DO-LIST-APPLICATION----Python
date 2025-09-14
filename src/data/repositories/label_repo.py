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