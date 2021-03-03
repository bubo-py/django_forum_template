from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_avatar = models.ImageField(upload_to='user_avatars', default='default_avatar.png')

    def __str__(self):
        return self.user.username
