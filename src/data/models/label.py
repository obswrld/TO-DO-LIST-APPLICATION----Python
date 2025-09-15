from src.schemas.extensions import db

task_label = db.Table(
    'task_label',
    db.metadata,
    db.Column("task_id", db.Integer, db.ForeignKey("task.id"), primary_key=True),
    db.Column("label_id", db.Integer, db.ForeignKey("label.id"), primary_key=True),
    extend_existing=True
)


class Label(db.Model):
    __tablename__ = 'label'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }