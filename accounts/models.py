

# Create your models here.
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    imageprofil = models.ImageField(
        upload_to='profile_images/',  # dossier de stockage
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.username
