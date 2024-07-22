from django.db import models
from users.models import User

class Task(models.Model):
    TASK_CHOICES = [
        ('ToDo', 'to do'),
        ('Doing', 'doing'),
        ('Done', 'done'),
    ]
    
    name = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='author_tasks', on_delete=models.CASCADE)
    executant = models.ForeignKey(User, related_name='executant_tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_type = models.CharField(choices=TASK_CHOICES, default='ToDo', max_length=6)

    def __str__(self) -> str:
        return self.name
