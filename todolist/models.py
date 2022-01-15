from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    title =  models.CharField(max_length  = 200)
    description = models.TextField()
    isdone = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title