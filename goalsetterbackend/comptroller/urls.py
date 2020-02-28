from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserView, name='users')
router.register(r'', views.GoalView, name='goals')
router.register(r'', views.TaskView, name='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework'))
]