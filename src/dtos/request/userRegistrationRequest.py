class UserRegistrationRequest:
    def __init__(self, username:str, email:str, password:str):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }