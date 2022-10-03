from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

# Create your views here.

def TaskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'Tasks/home.html', {'tasks' : tasks})

def AddTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addTask.html', {'forms' : form})