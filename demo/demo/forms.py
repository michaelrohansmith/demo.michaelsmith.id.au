from django import forms

from demo import models

class TaskForm(forms.Form):
    name = forms.CharField()
#    next = forms.ModelMultipleChoiceField(queryset=models.Task.objects.all())
    status = forms.MultipleChoiceField(models.Task.STATUS_CHOICES)
    start_here = forms.BooleanField()
