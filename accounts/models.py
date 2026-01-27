

# Create your models here.
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass



# class User(AbstractUser):
#     imageprofil = models.ImageField(
#         upload_to='profile_images/',  # dossier de stockage
#         null=True, 
#         blank=True
#     )

#     def __str__(self):
#         return self.username



# from django.contrib.auth.models import AbstractUser
# from django.db import models


# class User(AbstractUser):
#     imageprofil = models.ImageField(upload_to='profile_images/', null=True, blank=True)

#     def __str__(self):
#         return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    # IMPORTANT: blank=True ET null=True pour éviter les erreurs
    imageprofil = CloudinaryField(
        "imageprofil",
        blank=True,
        null=True,
        folder="profiles"  # Optionnel mais recommandé
    )

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'accounts_user'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
