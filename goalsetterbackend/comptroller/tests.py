from django.test import TestCase
from comptroller.models import User
import json

# Create your tests here.
class UserTestCase(TestCase):
    GOALS = {
        "Goals": {
            "Goal": {
                "Name": "Run a marathon.",
                "Tasks Completed": "None",
                "Description": "My plan is to run faster than everyone else.",
                "Flat Goal": "Run a marathon in 20min.",
                "Schedule": "None"
            }
        }
    }

    def setUp(self):
        User.objects.create(email="user@email.com", password="12345", goals=json.dumps(self.GOALS))

    def test_user_goal_is_to_run_a_marathon(self):
        user = User.objects.get(email="user@email.com")
        self.assertEqual(self.GOALS, user.get_goals())
