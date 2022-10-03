from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList, name='Task-List'),
    path('addTask', views.AddTask, name='Add-Task'),
    path('editTask/<int:id>', views.EditTask, name='Edit-Task')
]
