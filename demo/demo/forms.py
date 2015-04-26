from django import forms

from demo import models

class TaskForm(forms.Form):
    name = forms.CharField()
    next = forms.ModelMultipleChoiceField(queryset=models.Task.objects.all())
    is_active = forms.BooleanField(required=False)
    start_here = forms.BooleanField(required=False)
