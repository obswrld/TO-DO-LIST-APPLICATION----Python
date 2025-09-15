class UserResponse:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @classmethod
    def from_model(cls, user):
        return cls(
            id=user.id,
            username = user.username,
            email = user.email
        )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }