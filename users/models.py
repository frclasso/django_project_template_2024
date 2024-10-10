from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/default/man_default.png', upload_to=f'profile_pics') # profile_pics/username/

    def __str__(self):
        return f'{self.user.username} profile.'

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            outpusize = (300,300)
            img.thumbnail(outpusize)
            img.save(self.image.path)
