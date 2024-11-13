# todo/forms.py
from django import forms
from .models import TaskItem

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = ['title', 'completed']
