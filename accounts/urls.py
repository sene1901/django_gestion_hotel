# # accounts/urls.py
# from django.urls import path
# from .views import (
#     RegisterView,
#     ProfileView,
#     PasswordResetRequestView,
#     SetNewPasswordView,
#     ProfileImageUpdateView,
#     LogoutView,
#     EmailLoginView,
# )
# from rest_framework_simplejwt.views import TokenRefreshView

# urlpatterns = [
#     path("register/", RegisterView.as_view()),

#     #  LOGIN 
#     path("login/", EmailLoginView.as_view()),

#     #  refresh JWT
#     path("refresh/", TokenRefreshView.as_view()),

#     #  profil
#     path("profile/", ProfileView.as_view()),

#     #  reset password
#     path("password-reset/", PasswordResetRequestView.as_view()),
#     path("password-reset-confirm/", SetNewPasswordView.as_view()),

#     #  logout
#     path("logout/", LogoutView.as_view(), name="logout"),

#     #  photo profil
#     path("profile/image/", ProfileImageUpdateView.as_view(), name="profile-image-update"),
# ]
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
    # Inscription
    path("register/", RegisterView.as_view(), name="register"),
    
    # Connexion
    path("login/", EmailLoginView.as_view(), name="login"),
    
    # Refresh JWT
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # Profil
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/image/", ProfileImageUpdateView.as_view(), name="profile-image-update"),
    
    # Reset password
    path("password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    path("password-reset-confirm/", SetNewPasswordView.as_view(), name="password-reset-confirm"),
    
    # Logout
    path("logout/", LogoutView.as_view(), name="logout"),
]