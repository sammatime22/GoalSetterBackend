from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GoalSerializer, TaskSerializer
from .models import User, Goal, Task
# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class GoalView(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
