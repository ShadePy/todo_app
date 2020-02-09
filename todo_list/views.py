from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm


def index(request):

    list_of_todos = Todo.objects.all()

    form = TodoForm()

    context = {"list_of_todos": list_of_todos, "form": form}

    return render(request, "index.html", context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST["text"])
        new_todo.save()

    return redirect("home")


def todo_change(request, todo_id):
    a_todo = Todo.objects.get(pk=todo_id)
    if a_todo.complete:
        a_todo.complete = False
    else:
        a_todo.complete = True
    a_todo.save()

    return redirect("home")


def delete_complete(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect("home")


def delete_all(request):
    Todo.objects.all().delete()

    return redirect("home")
