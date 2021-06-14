from django.urls import path

from to_do.to_do_app.views import index, create_todo, change_todo_state, delete_todo

urlpatterns = [
    path('', index),
    path('todos-add/', create_todo),
    path('todo-change-state/<int:pk>', change_todo_state),
    path('todo-delete/<int:pk>', delete_todo),
]
