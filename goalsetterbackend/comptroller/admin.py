from django.contrib import admin
from .models import User, Goal, Task
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    user_attr_display = ('email', 'password')

class GoalAdmin(admin.ModelAdmin):
    goal_attr_display = ('user', 'name', 'tasks_completed', 'description', 'flat_goal')

class TaskAdmin(admin.ModelAdmin):
    task_attr_display = ('goal', 'time', 'completed', 'name', 'notes')

admin.site.register(User, UserAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Task, TaskAdmin)