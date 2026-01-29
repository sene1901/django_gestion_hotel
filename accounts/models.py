

# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from cloudinary.models import CloudinaryField


# class User(AbstractUser):
#     # IMPORTANT: blank=True ET null=True pour éviter les erreurs
#     imageprofil = CloudinaryField(
#         "imageprofil",
#         blank=True,
#         null=True,
#         folder="profiles"  # Optionnel mais recommandé
#     )

#     def __str__(self):
#         return self.username
    
#     class Meta:
#         db_table = 'accounts_user'
#         verbose_name = 'Utilisateur'
#         verbose_name_plural = 'Utilisateurs'
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone


# -----------------------------
# Custom User Manager
# -----------------------------
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email doit être fourni")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Le superuser doit avoir is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Le superuser doit avoir is_superuser=True")

        return self.create_user(email, password, **extra_fields)


# -----------------------------
# Custom User
# -----------------------------
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    imageprofil = CloudinaryField(
        "imageprofil",
        blank=True,
        null=True,
        folder="profiles"
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # username requis pour AbstractBaseUser

    def __str__(self):
        return self.email

    class Meta:
        db_table = "accounts_user"
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

