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
    
    def __str__(self):
        """
        This method simply returns the eamil back as a string.

        @return String The email as a string.
        """
        return self.email

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

    def __str__(self):
        """
        This method simply returns the name back as a string.

        @return String The name as a string.
        """
        return self.name

    def get_info(self):
        """
        This method returns back a JSON object equivalent of the Goal data.

        @return JSON Object A JSON object equivalent of the Goal data.
        """
        return {
            "Name": self.name,
            "Tasks Completed": self.tasks_completed,
            "Description": self.description,
            "Flat Goal": self.flat_goal
        }

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

    def __str__(self):
        """
        This method simply returns the name back as a string.

        @return String The name as a string.
        """
        return self.name

    def get_info(self):
        """
        This method returns back a JSON object equivalent of the Task data.

        @return JSON Object A JSON object equivalent of the Task data.
        """
        return {
            "Name": self.name,
            "Time": self.time,
            "Completed": self.completed,
            "Notes": self.notes
        }
