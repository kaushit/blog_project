from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
# from django.shortcuts import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ResizedImageField(upload_to='profile_pic',
                              default='default.png', size=[300, 300], crop=['middle', 'center'])

    def __str__(self):
        return f'{self.user.username} Profile'
