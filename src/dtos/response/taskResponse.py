class TaskResponse:
    def __init__(self, id, title, description, user_id, created_at, updated_at):
        self.id = id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_model(cls, task):
        return cls(
            id=task.id,
            title=task.title,
            description=task.description,
            user_id=task.user_id,
            created_at=task.created_at,
            updated_at=task.updated_at
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }