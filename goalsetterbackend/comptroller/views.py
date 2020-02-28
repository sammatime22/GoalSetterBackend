from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, GoalSerializer, TaskSerializer
from .models import User, Goal, Task
# Create your views here.

class UserView(viewsets.ModelViewSet):
    """
    A serializer for User objects.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GoalView(viewsets.ModelViewSet):
    """
    A serializer for Goal objects.
    """
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()

class TaskView(viewsets.ModelViewSet):
    """
    A serializer for Task objects.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


@api_view(['GET'])
def get_user_info(request):
    """
    This method will return all of a user's goals and tasks.
    """
    email = "fail"
    print(request.body)
    print(email)

    data = json.loads(request.body.decode("utf-8"))

    email = data["email"]
    password = data["password"]
    
    print(data)
    try:
        user = User.objects.get(email=email)

        # Deny requests to our API that have the wrong credentials
        if user.password != password:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # Return goal and task data to requests with appropriate credentials
        else:
            response = {}
            goals = Goal.objects.get(user)
            # Develop the JSON response
            for goal in goals:
                goal_object_to_add = {}
                tasks = Task.objects.get(goal)
                # Retrieve and add all Tasks for a specific Goal
                for task in tasks:
                    goal_object_to_add["Tasks"][str(task)] = task.get_info()
                # Add the associated Goal
                response["Goals"][str(goal)] = goal.get_info()
            return JsonResponse(response)
    # If the user does not exist, return 404
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
