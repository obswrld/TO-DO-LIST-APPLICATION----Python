from src.schemas import db

task_label = db.Table(
    'task_label',
    db.Column("task_id", db.Integer, db.ForeignKey("task_id"), primary_key=True),
    db.Column("label_id", db.Integer, db.ForeignKey("label_id"), primary_key=True)
)

class Label(db.Model):
    __tablename__ = 'label'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }