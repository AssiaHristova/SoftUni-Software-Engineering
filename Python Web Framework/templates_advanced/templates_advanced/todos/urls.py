from django.urls import path

from templates_advanced.todos.views import list_todos, create_todo

urlpatterns = [
    path('', list_todos, name='todos list'),
    path('create/', create_todo, name='create todo')
]
