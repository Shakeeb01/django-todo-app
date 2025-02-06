from django.shortcuts import render,redirect,get_object_or_404
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


# Delete Task
def delete_task(request,id):
    task = get_object_or_404(Task,pk = id)
    task.delete()
    messages.success(request,'You Task Has Been Deleted Successfully!')
    return redirect(reverse('all_tasks'))


# Update Existing Task

def update_task(request,id):
    task  = get_object_or_404(Task, pk = id)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Task Has Been Updated Successfully!')
            return redirect(reverse('all_tasks'))
        
    else:
        form = TaskForm(instance=task)
        
    return render(request,'task/update_task.html',{'form':form})