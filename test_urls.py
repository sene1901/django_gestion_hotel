import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_django.settings')  # Remplacez 'config' par le nom de votre projet
django.setup()

from django.urls import get_resolver

def show_urls(urlpatterns, depth=0):
    for pattern in urlpatterns:
        if hasattr(pattern, 'url_patterns'):
            show_urls(pattern.url_patterns, depth + 1)
        else:
            print('  ' * depth + str(pattern.pattern))

urlconf = __import__(os.environ['DJANGO_SETTINGS_MODULE'], {}, {}, ['']).ROOT_URLCONF
resolver = get_resolver(urlconf)
show_urls(resolver.url_patterns)