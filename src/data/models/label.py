from src.schemas import db

task_label = db.Table(
    'task_label',
    db.column("task_id", db.Integer, db.ForeignKey("task_id"), primary_key=True),
    db.column("label_id", db.Integer, db.ForeignKey("label_id"), primary_key=True)
)

class Label(db.model):
    __tablename__ = 'label'

    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100), unique=True, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }