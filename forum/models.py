from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ForumThread(models.Model):
    thread_heading = models.CharField(max_length=100)
    thread_content = models.TextField(max_length=750)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
