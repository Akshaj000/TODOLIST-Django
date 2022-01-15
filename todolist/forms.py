from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description','isdone')


# class CheckForm(forms.ModelForm):
    
#     class Meta:
#         model = Task
#         fields = ('isdone',)