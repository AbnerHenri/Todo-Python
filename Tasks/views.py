from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Task
from .forms import TaskForm

# Create your views here.

def TaskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'Tasks/home.html', {'tasks' : tasks})

def AddTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/addTask.html', {'forms' : form})


def EditTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'Tasks/editTask.html', {'forms': form, 'task': task})
            
    else:
        return render(request, 'Tasks/editTask.html', {'forms': form, 'task': task})


def DelTask(request, id):
        task = get_object_or_404(Task, pk=id)
        task.delete()
        
        messages.info(request, 'Tarefa deletada com sucesso')

        return redirect('/')
