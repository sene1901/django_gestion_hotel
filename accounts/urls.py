from django.urls import path
from .views import (
    ProfileView,
    ProfileImageUpdateView,
    LogoutView,
    # On garde seulement ce qui n'est pas géré par Djoser
)

urlpatterns = [
    # Profil (votre logique custom)
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/image/", ProfileImageUpdateView.as_view(), name="profile-image-update"),
    
    # Logout (votre logique custom si nécessaire)
    path("logout/", LogoutView.as_view(), name="logout"),
    
   
]