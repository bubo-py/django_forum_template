from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_avatar = models.ImageField(upload_to='user_avatars', default='default_avatar.png')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        image_path = self.user_avatar.path

        i = Image.open(image_path)

        if i.width > 200 or i.height > 200:
            new_size = (200, 200)
            i.thumbnail(new_size)
            i.save(image_path)
