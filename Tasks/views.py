from django.shortcuts import render

# Create your views here.

def TaskList(request):
    return render(request, 'Tasks/Home.html')
