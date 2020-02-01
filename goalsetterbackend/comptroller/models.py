from django.db import models

# Create your models here.

class User(models.Model):
    """
    The basic user model.

    @param email - The email of the user.
    @param password - The password of the user.
    @param goals - A list of Goal objects that will be related to 
                   the user.
    """
    email = models.EmailField()
    password = models.CharField(max_length=100)
    goals = []


class Goal(models.Model):
    """
    The definition of a Goal as precieved by the end user.

    @param name - The name of the goal.
    @param tasks_completed - The number of tasks relative to the 
                             goal that have been completed.
    @param description - The description of the goal.
    @param flat_goal - The most basic definition of the goal.
    @param schedule - A list of Task objects related to the goal.
    """
    name = models.CharField(max_length=200)
    tasks_completed = models.IntegerField()
    description = models.TextField()
    flat_goal = models.CharField(max_length=200)
    schedule = []


class Task(models.Model):
    """
    The definition of a Task as based on a Goal.

    @param time - The time the task is to be/was completed.
    @param completed - A boolean representing if the task is done.
    @name - The name of the task.
    @related_goal - The goal that this task is related to.
    @notes - Notes pertaining to the task.
    """
    time = models.DateField()
    completed = models.BooleanField()
    name = models.CharField(max_length=200)
    related_goal = models.CharField(max_length=200)
    notes = models.TextField()
