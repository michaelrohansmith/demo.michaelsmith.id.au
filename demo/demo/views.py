from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from datetime import datetime

from demo import models, forms

# Views for demo application

def get_status_value(symbol):
    if symbol == u'I':
        return 'Inactive'
    if symbol == u'A':
        return 'Active'
    return None

# The main page
def default_page(request):
    tasks = list()
    for task in models.Task.objects.all():
        task_dict = dict()
        task_dict['name'] = task.name
        task_dict['next'] = task.next
        task_dict['status'] = models.Task.get_status_display(task)
        task_dict['start_here'] = task.start_here
        tasks.append(task_dict)
    context = {'tasks': tasks}
    return render(request, 'demo/index.html', context)

#
# Manage Tasks
#
# Create a block of text in an task
def task_add(request):
    print 'task_add: 1'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print 'task_add: 2'
            # process the data in form.cleaned_data as required
            task = models.Task()
            task.name = form.cleaned_data['name']
            if 'next' in form.cleaned_data:
                task.next = form.cleaned_data['next']
            else:
                task.next = None
            task.status = form.cleaned_data['status']
            task.start_here = form.cleaned_data['start_here']
            task.save()
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.TaskForm()
        return render(request, 'demo/task_form.html', {'form': form})

# Detail for Task
class TaskDetail(generic.DetailView):
    model = models.Task

# Update Task
class TaskUpdate(UpdateView):
    model = models.Task
    fields = ['name', 'next', 'status', 'start_here']

# Delete Task item
class TaskDelete(DeleteView):
    model = models.Task
    success_url = reverse_lazy('list')
