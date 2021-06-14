from django.shortcuts import render, redirect

from to_do.to_do_app.models import ToDo
from to_do.to_do_app.models.to_do_models import Person


def index(request):
    context = {
        'todos': ToDo.objects.all(),
    }
    return render(request, 'index.html', context)


def create_todo(request):
    text = request.POST['text']
    description = request.POST['description']
    owner_name = request.POST['owner']
    owner = Person.objects.filter(name=owner_name).first()
    if not owner:
        owner = Person(name=owner_name)
        owner.save()

    todo = ToDo(
        text=text,
        description=description,
        owner=owner,
    )
    todo.save()
    return redirect('/')


def change_todo_state(request, pk):
    todo = ToDo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect('/')


def delete_todo(request, pk):
    todo = ToDo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')

