from datetime import datetime
from src.schemas.extensions import db
from src.data.models.label import task_label

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean,  default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    labels = db.relationship('Label', secondary='task_label', backref='tasks', lazy='dynamic')

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id



    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id,
        }

    def __repr__(self):
        return f'<Task {self.title}, completed: {self.completed}, created_at: {self.created_at}, user_id: {self.user_id}>'