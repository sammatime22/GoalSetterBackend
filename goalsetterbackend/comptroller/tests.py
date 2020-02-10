from django.test import TestCase
from comptroller.models import User
import json

# Create your tests here.
class UserTestCase(TestCase):
    # A Mock Goals JSON Object
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

    user = None

    def setUp(self):
        User.objects.create(email="user@email.com", password="12345", goals=\
            json.dumps(self.GOALS))
        self.user = User.objects.get(email="user@email.com")

    def test_00_user_password_checks_out(self):
        self.assertEqual("12345", self.user.password)

    def test_01_user_goal_is_to_run_a_marathon(self):
        self.assertEqual(self.GOALS, self.user.get_goals())

    def test_02_user_goal_not_written_in_json_becomes_nothing(self):
        User.objects.create(email="baduser@bad.com", password="54321", goals=\
            "Eat a cherry pie.")
        bad_user = User.objects.get(email="baduser@bad.com")
        self.assertEqual({"Goals": "None"}, bad_user.get_goals())

