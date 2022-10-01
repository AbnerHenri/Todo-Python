from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList, name='Task-List'),
    path('yourName/<str:name>', views.YourName, name='Your-Name')
]
