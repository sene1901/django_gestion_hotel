from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser - Authentification + Activation + Password Reset
    path('auth/', include('djoser.urls')),      # Endpoints de base
    path('auth/', include('djoser.urls.jwt')),  # Endpoints JWT
    
    # Vos apps
    path('accounts/', include('accounts.urls')),
    path('hotels/', include('hotels.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)