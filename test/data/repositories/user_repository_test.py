import unittest
from src.data.models.user import User
from src.data.repositories.user_repositories import UserRepository
from src.schemas.db import db

class TestUserRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_repository = UserRepository()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()

    def test_save_user(self):
        user = User(username="obswrld22", email="republicoba1@gamil.com")
        save_user = self.user_repository.save_user(user)
        self.assertEqual(save_user.username, "obswrld22")