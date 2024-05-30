from rest_framework import generics
from . import models
from . import serializers
from django.http import JsonResponse

# Create your views here.


class TodoListCreate(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


def todo_list(request):
    todos = models.Todo.objects.all()
    todo_as_json = serializers.TodoSerializer(todos, many=True).data

    return JsonResponse({'todos': todo_as_json})
