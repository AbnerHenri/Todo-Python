from django.shortcuts import render

# Create your views here.

def TaskList(request):
    return render(request, 'Tasks/home.html')

def YourName(request, name):
    return render(request, 'Tasks/yourName.html', {'name' : name})
