from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ForumThread(models.Model):
    heading = models.CharField(max_length=100)
    content = models.TextField(max_length=750)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading
