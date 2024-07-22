from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'content', 'author', 'executant', 'created_at', 'updated_at', 'task_type']