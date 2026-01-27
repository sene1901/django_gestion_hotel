
# from django.db import models
# from django.conf import settings
# from cloudinary.models import CloudinaryField


# class Hotel(models.Model):
#     owner = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='hotels'
#     )
#     name = models.CharField(max_length=150)
#     description = models.TextField()
#     prix = models.DecimalField(max_digits=10, decimal_places=2)
    
#     # Image stockée sur Cloudinary - utilise CloudinaryField
#     image = CloudinaryField(
#         'image',
#         folder='hotels/',  # Dossier dans Cloudinary
#         null=True,
#         blank=True
#     )
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class Hotel(models.Model):
    DEVISE_CHOICES = [
        ('XOF', 'F XOF'),
        ('EUR', 'EUR'),
        ('USD', 'USD'),
    ]
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='hotels'
    )
    name = models.CharField(max_length=150)
    description = models.TextField()
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    devise = models.CharField(max_length=3, choices=DEVISE_CHOICES, default='XOF')
    
    # Image stockée sur Cloudinary - utilise CloudinaryField
    image = CloudinaryField(
        'image',
        folder='hotels/',  # Dossier dans Cloudinary
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name