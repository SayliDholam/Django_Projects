from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    form = TaskForm()
    return render(request, 'ToDo/index.html', {'form': form, 'tasks': tasks})

@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('task_list')

def update_status(request, task_id, status):
    task = get_object_or_404(Task, pk=task_id)
    task.status = status
    task.save()
    return JsonResponse({'success': True, 'status': task.status})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')
