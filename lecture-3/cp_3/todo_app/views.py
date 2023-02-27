from django.shortcuts import render

from rest_framework import generics
from .models import TodoList, Todo
from .serializers import TodoListSerializer, TodoSerializer


class TodoListListCreate(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListTodosListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        todo_list_id = self.kwargs['todo_list_id']
        return Todo.objects.filter(todo_list_id=todo_list_id)

    def perform_create(self, serializer):
        todo_list_id = self.kwargs['todo_list_id']
        todo_list = TodoList.objects.get(id=todo_list_id)
        serializer.save(todo_list=todo_list)


class TodoListTodosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

