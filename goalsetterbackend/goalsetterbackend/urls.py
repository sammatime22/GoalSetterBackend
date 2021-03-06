"""goalsetterbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from rest_framework import routers
from comptroller import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'user')
router.register(r'goals', views.GoalView, 'goal')
router.register(r'tasks', views.TaskView, 'task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/', include(router.urls)),
    
    # REST API
    url(
        r'get-user-info/',
        views.get_user_info,
        name='get_user_info'
    )
]
