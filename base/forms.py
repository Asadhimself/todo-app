from django import forms

from base.models import Task


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {"deadline":
                       forms.DateTimeInput(attrs={'type': 'datetime-local'})}
        fields = ['title', 'description', 'deadline', 'complete']
