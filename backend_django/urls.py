# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # Djoser - Authentification + Activation + Password Reset
#     path('api/auth/', include('djoser.urls')),      # Endpoints de base
#     path('api/auth/', include('djoser.urls.jwt')),  # Endpoints JWT
    
#     # Vos apps
#     path('api/accounts/', include('accounts.urls')),
#     path('api/hotels/', include('hotels.urls')),
#     path('', include('core.urls')),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Debug: afficher les URLs chargées
if settings.DEBUG:
    from django.urls import get_resolver
    print("=" * 50)
    print("URLs chargées:")
    resolver = get_resolver()
    for pattern in resolver.url_patterns:
        print(f"  - {pattern}")
    print("=" * 50)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Djoser
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    
    # Vos apps
    path('api/accounts/', include('accounts.urls')),
    path('api/hotels/', include('hotels.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)