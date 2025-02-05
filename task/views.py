from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .models import Task
from .forms import TaskForm

# _________________________________________________________ #

# Main Home View
def home_view(request):
    return render(request,'base.html')


# List of All Tasks
def tasks_list(request):
    context = {}
    all_tasks = Task.objects.all()
    context['all_tasks'] = all_tasks
    return render(request,'task/tasks_list.html',context)


# Create Task
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Task Has Been Created Successfully!')
            return redirect(reverse('all_tasks'))
        
    else:
        form = TaskForm()        
    return render(request,'task/create_task.html',{'form' : form})