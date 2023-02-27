from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoListSerializer

@api_view(['GET'])
def todo_lists(request):
    todo_lists = TodoList.objects.all()
    serializer = TodoListSerializer(todo_lists, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo_list(request):
    serializer = TodoListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def todo_list_detail(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    serializer = TodoListSerializer(todo_list)
    return Response(serializer.data)

@api_view(['PUT'])
def update_todo_list(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    serializer = TodoListSerializer(instance=todo_list, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_todo_list(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    todo_list.delete()
    return Response(status=204)

@api_view(['GET'])
def todo_list_todos(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    todos = todo_list.todos.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(todo_list=todo_list)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo_without_list(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def todo_detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)

@api_view(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
