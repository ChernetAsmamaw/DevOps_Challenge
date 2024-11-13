# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TaskItem
from .forms import TaskForm

@login_required
def todo_list(request):
    tasks = TaskItem.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user  # Set the owner to the logged-in user
            task.user = request.user   # Set the user field to the logged-in user as well
            task.save()
            return redirect('todo:todo_list')  # Redirect to the todo list after adding the task
    else:
        form = TaskForm()
    return render(request, 'todo/todo_form.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(TaskItem, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/todo_form.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(TaskItem, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('todo:todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'task': task})
