class TaskResponse:
    def __init__(self, title, description, user_id, created_at, updated_at):
        self.title = title
        self.description = description
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_model(cls, task):
        return cls(
            task.title,
            task.description,
            task.user_id,
            task.created_at,
            task.updated_at
        )

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }