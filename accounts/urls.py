# accounts/urls.py
from django.urls import path
from .views import (
    RegisterView,
    ProfileView,
    PasswordResetRequestView,
    SetNewPasswordView,
    ProfileImageUpdateView,
    LogoutView,
    EmailLoginView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view()),

    #  LOGIN 
    path("login/", EmailLoginView.as_view()),

    #  refresh JWT
    path("refresh/", TokenRefreshView.as_view()),

    #  profil
    path("profile/", ProfileView.as_view()),

    #  reset password
    path("password-reset/", PasswordResetRequestView.as_view()),
    path("password-reset-confirm/", SetNewPasswordView.as_view()),

    #  logout
    path("logout/", LogoutView.as_view(), name="logout"),

    #  photo profil
    path("profile/image/", ProfileImageUpdateView.as_view(), name="profile-image-update"),
]
