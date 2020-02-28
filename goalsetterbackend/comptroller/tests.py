from django.urls import reverse
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from comptroller.models import User, Goal, Task
import json

# Create your tests here.
class UserTestCase(TestCase):

    user = None

    client = Client()

    def setUp(self):
        """
        Setting up the user object which will be used in the remainder of the 
        tests.
        """
        User.objects.create(email="user@email.com", password="12345")
        self.user = User.objects.get(email="user@email.com")

    def test_00_user_password_checks_out(self):
        """
        Checking that we can grab the correct password for the correct user.
        """
        self.assertEqual("12345", self.user.password)

    def test_01_relate_goal_to_user(self):
        """
        Checking that we can relate a goal to a user, and return it back with a 
        parameter of said user.
        """
        goal_a = Goal.objects.create(user=User.objects.get(email="user@email.com"),\
            name="Pass JLPT N2", tasks_completed=2, description="The N2 exam \
            gives me a goal to get over my current study slump.", flat_goal=\
            "Get a perfect score on the exam.")
        self.assertEqual("Pass JLPT N2", Goal.objects.get(user=User.objects.get(\
            email="user@email.com")).name)
    
    def test_02_relate_task_to_goal(self):
        """
        Checking that we can relate a task to a goal and retrieve said task with 
        the user account.
        """
        Goal.objects.create(user=User.objects.get(email="user@email.com"),\
            name="Pass JLPT N2", tasks_completed=2, description="The N2 exam \
            gives me a goal to get over my current study slump.", flat_goal=\
            "Get a perfect score on the exam.")
        Task.objects.create(goal=Goal.objects.get(name="Pass JLPT N2"), time=\
            '2020-02-15 22:10:00', completed=False, name="Grammar Study",\
            notes="We should be able to understand \'ni sai shite\'.")
        self.assertFalse(Task.objects.get(goal=Goal.objects.get(name=\
            "Pass JLPT N2")).completed)


class ComptrollerAPITests(APITestCase):
    
    def setUp(self):
        """
        Setting up the user object which will be used in the remainder of the 
        tests.
        """
        User.objects.create(email="user@email.com", password="12345")
        Goal.objects.create(user=User.objects.get(email="user@email.com"),\
            name="Pass JLPT N2", tasks_completed=2, description="The N2 exam \
            gives me a goal to get over my current study slump.", flat_goal=\
            "Get a perfect score on the exam.")

    def test_04_api_get_generic_user_goals_succeeds(self):
        """
        This test checks that another application, if providing authentication,
        can gather the goals of a generic user.
        """
        response = self.client.get(reverse('users'), 
            content_type='application/json'
        )
        print(response)
