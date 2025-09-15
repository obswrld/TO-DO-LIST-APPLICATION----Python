from datetime import datetime
from src.schemas.extensions import db
from src.data.models.label import task_label

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    labels = db.relationship('Label', secondary='task_label', backref='tasks', lazy='dynamic')


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'created_at': self.created_at,
            'user_id': self.user_id,
            'labels': self.labels,
        }

    def __repr__(self):
        return f'<Task {self.title}, completed: {self.completed}, created_at: {self.created_at}, user_id: {self.user_id}>'