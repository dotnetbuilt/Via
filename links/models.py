from django.db import models
from users.models import User

class Link(models.Model):
    link = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='links', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link