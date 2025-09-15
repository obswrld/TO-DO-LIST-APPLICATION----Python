import unittest
from venv import create

from src.data.models.user import User
from src.data.repositories.user_repositories import UserRepository
from src.schemas.extensions import db

class TestUserRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app.app_context().push()
        cls.user_repository = UserRepository()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_save_user(self):
        user = User(username="obswrld22", email="republicoba1@gamil.com")
        save_user = self.user_repository.save_user(user)
        self.assertEqual(save_user.username, "obswrld22")