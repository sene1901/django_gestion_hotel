# check_urls.py
import os
import django

# Adaptez 'config.settings' selon votre structure (peut-être 'settings' ou 'backend.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.urls import get_resolver

def show_urls(urlpatterns, prefix=''):
    for pattern in urlpatterns:
        if hasattr(pattern, 'url_patterns'):
            show_urls(pattern.url_patterns, prefix + str(pattern.pattern))
        else:
            print(prefix + str(pattern.pattern))

resolver = get_resolver()
show_urls(resolver.url_patterns)