from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# Ajoutez ceci temporairement
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser - Authentification + Activation + Password Reset
    path('api/auth/', include('djoser.urls')),      # Endpoints de base
    path('api/auth/', include('djoser.urls.jwt')),  # Endpoints JWT
    
    # Vos apps
    path('api/accounts/', include('accounts.urls')),
    path('api/hotels/', include('hotels.urls')),
    path('', include('core.urls')),
]




# Dans urls.py principal


def list_urls(request):
    from django.urls import get_resolver
    resolver = get_resolver()
    patterns = []
    
    def collect_patterns(pattern_list, prefix=''):
        for pattern in pattern_list:
            if hasattr(pattern, 'url_patterns'):
                collect_patterns(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                patterns.append(prefix + str(pattern.pattern))
    
    collect_patterns(resolver.url_patterns)
    return JsonResponse({'urls': patterns})

urlpatterns = [
    path('debug/urls/', list_urls),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)