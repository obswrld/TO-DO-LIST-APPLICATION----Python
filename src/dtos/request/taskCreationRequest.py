class TaskCreationRequest:
    def __init__(self, title:str, description:str, user_id:int):
        self.title = title
        self.description = description
        self.user_id = user_id

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "user_id": self.user_id,
        }
