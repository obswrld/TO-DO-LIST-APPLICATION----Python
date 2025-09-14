class UserResponse:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    @classmethod
    def from_model(cls, user):
        return cls(
            id=user.id
            ,username = user.username
            ,email = user.email
        )

    def to_dict(self):
        return {
            "user_id": self.user_id
            ,"username": self.username
            ,"email": self.email
        }