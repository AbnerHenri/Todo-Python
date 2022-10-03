from django.shortcuts import render

from .models import Task

# Create your views here.

def TaskList(request):
    tasks = Task.objects.all()
    return render(request, 'Tasks/home.html', {'tasks' : tasks})