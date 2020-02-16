from django.db import models
import json

# Create your models here.

class User(models.Model):
    """
    The basic user model.

    @param email - The email of the user.
    @param password - The password of the user.
    """
    email = models.EmailField()
    password = models.CharField(max_length=100)


class Goal(models.Model):
    """
    The definition of a Goal as precieved by the end user.

    @param user - A key to a user object that has said goal.
    @param name - The name of the goal.
    @param tasks_completed - The number of tasks relative to the 
                             goal that have been completed.
    @param description - The description of the goal.
    @param flat_goal - The most basic definition of the goal.
    @param schedule - A list of Task objects related to the goal.
    """
    user = models.ForeignKey('User', on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    tasks_completed = models.IntegerField()
    description = models.TextField()
    flat_goal = models.CharField(max_length=200)


class Task(models.Model):
    """
    The definition of a Task as based on a Goal.

    @param goal - The goal that this task is related to.
    @param time - The time the task is to be/was completed.
    @param completed - A boolean representing if the task is done.
    @name - The name of the task.
    @related_goal - The goal that this task is related to.
    @notes - Notes pertaining to the task.
    """
    goal = models.ForeignKey('Goal', on_delete=models.CASCADE, default=None)
    time = models.DateTimeField()
    completed = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    notes = models.TextField()
