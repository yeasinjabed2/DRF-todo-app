from django.urls import path
from .views import TodoListCreate, TodoRetrieveUpdateDestroy, todo_list


urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroy.as_view(),
         name='todo-retrieve-update-destroy'),
    path('todo-list/', todo_list, name='todo-list'),
]
