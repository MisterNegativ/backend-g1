from django.db import models

from django.db import models

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

