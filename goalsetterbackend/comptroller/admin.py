from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    user_attr_display = ('email', 'password', 'goals')

admin.site.register(User, UserAdmin)
