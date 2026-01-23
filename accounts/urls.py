# from django.urls import path , include
# from django.contrib.auth import views as auth_views
# from .views import RegisterView, MyTokenObtainPairView


# urlpatterns = [
#       path("login/", auth_views.LoginView.as_view(), name="login"),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('login/', MyTokenObtainPairView.as_view(), name='login'),

#     # Password reset
#     path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
# ]
from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('profile/', ProfileView.as_view()),
]

