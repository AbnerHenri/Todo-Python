from django import forms
from .models import Task

# Create your forms here

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')