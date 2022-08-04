from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=1000)
    date = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' - ' + self.description
