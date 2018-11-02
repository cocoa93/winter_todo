from django.shortcuts import render, get_object_or_404, redirect

from todo.models import Todo
from .forms import TodoForm
from django.utils import timezone
# Create your views here.


def todo_list(request):
    todo_objects = Todo.objects.all()
    now = timezone.now().date()
    todo_objects = sorted(todo_objects,key=lambda d: d.importance,reverse=True)
    return render(request,'todo/todo_list.html',{'todo_objects':todo_objects,'now':now,})


def todo_write(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_write.html', {'form': form})


def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect(todo_list)


def todo_check(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect(todo_list)


def todo_importance(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.importance = not todo.importance
    todo.save()
    return redirect(todo_list)


def todo_detail(request,pk):
    todo = Todo.objects.get(pk=pk)
    return render(request,'todo/todo_detail.html',{'todo':todo})