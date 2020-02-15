from django.test import TestCase
from comptroller.models import User
import json

# Create your tests here.
class UserTestCase(TestCase):

    user = None

    def setUp(self):
        User.objects.create(email="user@email.com", password="12345")
        self.user = User.objects.get(email="user@email.com")

    def test_00_user_password_checks_out(self):
        self.assertEqual("12345", self.user.password)
