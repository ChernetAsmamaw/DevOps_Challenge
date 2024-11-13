# todo/serializers.py
from rest_framework import serializers
from .models import TaskItem

class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ['id', 'user', 'title', 'completed', 'created_at', 'updated_at']
