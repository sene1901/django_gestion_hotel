

# from pathlib import Path
# from datetime import timedelta
# import os
# from decouple import config
# import dj_database_url

# CORS_ALLOW_ALL_ORIGINS = True
# BASE_DIR = Path(__file__).resolve().parent.parent

# # -----------------------------
# # Security
# # -----------------------------
# DEBUG = config('DEBUG', default=False, cast=bool)
# SECRET_KEY = config('SECRET_KEY')

# ALLOWED_HOSTS = [
#     "django-gestion-hotel.onrender.com",
#     ".onrender.com",
#     "127.0.0.1",
#     "localhost",
# ]

# # -----------------------------
# # Applications
# # -----------------------------
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
    
#     # Third-party apps
#     'rest_framework',
#     'rest_framework.authtoken',  # AVANT djoser
#     'rest_framework_simplejwt',
#     'rest_framework_simplejwt.token_blacklist',
#     'djoser',  
#     # 'django_rest_passwordreset',
#     'corsheaders',
#     'cloudinary',
#     'cloudinary_storage',
    
#     # Mes apps
#     'accounts.apps.AccountsConfig',
#     'hotels.apps.HotelsConfig',
# ]

# # -----------------------------
# # Middleware  ORDRE IMPORTANT !
# # -----------------------------
# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',  
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
# ]
# # Configuration Djoser

# # -----------------------------
# # Email Configuration (Gmail)
# # -----------------------------

# if DEBUG:
#     # En développement : emails dans la console
#     EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#     DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@monhotel.com')
# else:
#     # En production : Gmail SMTP
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     EMAIL_HOST = 'smtp.gmail.com'
#     EMAIL_PORT = 587
#     EMAIL_USE_TLS = True
#     EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Votre email Gmail
#     EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Mot de passe d'application
#     DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')  # Même email que ci-dessus
    
#     # Vérifier que Gmail est configuré
#     if not EMAIL_HOST_PASSWORD:
#         import warnings
#         warnings.warn(
#             "EMAIL_HOST_PASSWORD (Gmail) n'est pas configuré. Les emails ne seront pas envoyés.",
#             RuntimeWarning
#         )

# # -----------------------------
# # Configuration Djoser avec Gmail
# # -----------------------------
# GMAIL_CONFIGURED = bool(config('EMAIL_HOST_PASSWORD', default=''))

# DJOSER = {
#     'LOGIN_FIELD': 'email',
#     'USER_CREATE_PASSWORD_RETYPE': True,
#     'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
#     'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    
#     # Activation de compte (activé seulement si Gmail configuré)
#     'SEND_ACTIVATION_EMAIL': GMAIL_CONFIGURED and not DEBUG,
#     'SEND_CONFIRMATION_EMAIL': GMAIL_CONFIGURED and not DEBUG,
#     'ACTIVATION_URL': 'activate/{uid}/{token}',
    
#     # Reset password
#     'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
#     'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': False,
#     'PASSWORD_RESET_CONFIRM_RETYPE': True,
    
#     # URLs
#     'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    
#     # Configuration du site
#     'DOMAIN': config('FRONTEND_DOMAIN', default='localhost:5173'),
#     'SITE_NAME': config('SITE_NAME', default='Mon Hôtel'),
    
#     # Serializers
#     'SERIALIZERS': {
#         'user_create': 'djoser.serializers.UserCreateSerializer',
#         'user': 'djoser.serializers.UserSerializer',
#         'current_user': 'djoser.serializers.UserSerializer',
#         'user_delete': 'djoser.serializers.UserDeleteSerializer',
#     },
    
#     # Permissions
#     'PERMISSIONS': {
#         'user_create': ['rest_framework.permissions.AllowAny'],
#         'activation': ['rest_framework.permissions.AllowAny'],
#         'password_reset': ['rest_framework.permissions.AllowAny'],
#         'password_reset_confirm': ['rest_framework.permissions.AllowAny'],
#     },
    
#     # Templates d'email personnalisés (optionnel)
#     'EMAIL': {
#         'activation': 'email/activation.html',
#         'confirmation': 'email/confirmation.html',
#         'password_reset': 'email/password_reset.html',
#         'password_changed_confirmation': 'email/password_changed_confirmation.html',
#     },
# }
















# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# # -----------------------------
# # CORS CONFIGURATION  CRITIQUE
# # -----------------------------
# CORS_ALLOWED_ORIGINS = [
#     "https://django-hotel-eight.vercel.app",
#     "http://localhost:5173",
#     "http://localhost:3000",
# ]

# # Autorise toutes les preview URLs de Vercel
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://.*\.vercel\.app$",
# ]

# CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_METHODS = [
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
# ]

# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]

# # -----------------------------
# # CSRF CONFIGURATION
# # -----------------------------
# CSRF_TRUSTED_ORIGINS = [
#     "https://django-gestion-hotel.onrender.com",
#     "https://django-hotel-eight.vercel.app",
# ]

# #  Pour l'API REST, désactivez la protection CSRF sur les vues API
# # (utilisez @csrf_exempt ou rest_framework qui le gère automatiquement)

# # -----------------------------
# # REST Framework
# # -----------------------------
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',  # Par défaut pour l'inscription
#     ],
# }

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'ROTATE_REFRESH_TOKENS': True,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'UPDATE_LAST_LOGIN': True,  # ← Ajoutez 
    
#     'ALGORITHM': 'HS256',  # ← Ajoutez 
#     'SIGNING_KEY': SECRET_KEY,  # ← Ajoutez 
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
    
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
    
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
# }
# # -----------------------------
# # URL Configuration
# # -----------------------------
# ROOT_URLCONF = 'backend_django.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / "templates"],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'backend_django.wsgi.application'

# # -----------------------------
# # Database
# # -----------------------------
# DATABASES = {
#     'default': dj_database_url.config(default=config('DATABASE_URL'))
# }

# # -----------------------------
# # Authentication
# # -----------------------------
# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/accounts/login/'
# AUTH_USER_MODEL = 'accounts.User'

# # -----------------------------
# # Email
# # -----------------------------
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'noreply@monapp.com'

# # -----------------------------
# # Password validation
# # -----------------------------
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
# ]

# # -----------------------------
# # Internationalization
# # -----------------------------
# LANGUAGE_CODE = 'fr-fr'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # -----------------------------
# # Static files
# # -----------------------------
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # -----------------------------
# # Media files (Cloudinary)
# # -----------------------------
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# MEDIA_URL = '/media/'

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': config("CLOUD_NAME", default="doxx51hrh").strip(),
#     'API_KEY': config("CLOUD_API_KEY", default="167848852529489").strip(),
#     'API_SECRET': config("CLOUD_API_SECRET", default="3XzNJ_D839cOEKeVekUxLFteGoc").strip(),
# }

# # Configure cloudinary
# try:
#     import cloudinary
#     import cloudinary.uploader
#     import cloudinary.api
    
#     cloudinary.config(
#         cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
#         api_key=CLOUDINARY_STORAGE['API_KEY'],
#         api_secret=CLOUDINARY_STORAGE['API_SECRET'],
#         secure=True
#     )
# except ImportError:
#     pass

# # -----------------------------
# # Default primary key field type
# # -----------------------------
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# USE_X_FORWARDED_HOST = True




# # Email Backend - DÉVELOPPEMENT  (emails dans la console)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'noreply@monhotel.com'
# EMAIL_HOST_USER = 'noreply@monhotel.com'


from pathlib import Path
from datetime import timedelta
import os
from decouple import config
import dj_database_url

CORS_ALLOW_ALL_ORIGINS = True
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Security
# -----------------------------
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = [
    "django-gestion-hotel.onrender.com",
    ".onrender.com",
    "127.0.0.1",
    "localhost",
]

# -----------------------------
# Applications
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'corsheaders',
    'cloudinary',
    'cloudinary_storage',
    
    # Mes apps
    'accounts.apps.AccountsConfig',
    'hotels.apps.HotelsConfig',
]

# -----------------------------
# Middleware - ORDRE IMPORTANT !
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# Email Configuration (Gmail)
# -----------------------------
if DEBUG:
    # Développement : emails dans la console
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER', default='noreply@monhotel.com')
else:
    # Production : Gmail SMTP
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')
    SERVER_EMAIL = config('EMAIL_HOST_USER')
    EMAIL_TIMEOUT = 30
    
    # Vérifier que Gmail est configuré
    if not EMAIL_HOST_PASSWORD:
        import warnings
        warnings.warn(
            " EMAIL_HOST_PASSWORD (Gmail) non configuré. Les emails ne seront pas envoyés.",
            RuntimeWarning
        )

# -----------------------------
# Configuration Djoser
# -----------------------------
GMAIL_CONFIGURED = bool(config('EMAIL_HOST_PASSWORD', default=''))

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': False,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': False,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':False,
    
    # Activation de compte (activé seulement si Gmail configuré en production)
    'SEND_ACTIVATION_EMAIL': GMAIL_CONFIGURED and not DEBUG,
    'SEND_CONFIRMATION_EMAIL': GMAIL_CONFIGURED and not DEBUG,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    
    # Reset password
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': False,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    
    # URLs
    'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
    
    # Configuration du site
    'DOMAIN': config('FRONTEND_DOMAIN', default='localhost:5173'),
    'SITE_NAME': config('SITE_NAME', default='Mon Hôtel'),
    
    # Serializers
    'SERIALIZERS': {
        'user_create': 'djoser.serializers.UserCreateSerializer',
        'user': 'djoser.serializers.UserSerializer',
        'current_user': 'djoser.serializers.UserSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    
    # Permissions
    'PERMISSIONS': {
        'user_create': ['rest_framework.permissions.AllowAny'],
        'activation': ['rest_framework.permissions.AllowAny'],
        'password_reset': ['rest_framework.permissions.AllowAny'],
        'password_reset_confirm': ['rest_framework.permissions.AllowAny'],
    },
    
    # Templates d'email (assurez-vous qu'ils existent dans templates/email/)
    'EMAIL': {
        'activation': 'email/activation.html',
        'confirmation': 'email/confirmation.html',
        'password_reset': 'email/password_reset.html',
        'password_changed_confirmation': 'email/password_changed_confirmation.html',
    },
}
# DJOSER['SEND_ACTIVATION_EMAIL'] = False
# DJOSER['SEND_CONFIRMATION_EMAIL'] = False

SITE_ID = 1

# -----------------------------
# CORS Configuration - CRITIQUE
# -----------------------------
CORS_ALLOWED_ORIGINS = [
    "https://django-hotel-eight.vercel.app",
    "http://localhost:5173",
    "http://localhost:3000",
]

# Autorise toutes les preview URLs de Vercel
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.vercel\.app$",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# -----------------------------
# CSRF Configuration
# -----------------------------
CSRF_TRUSTED_ORIGINS = [
    "https://django-gestion-hotel.onrender.com",
    "https://django-hotel-eight.vercel.app",
]

# -----------------------------
# REST Framework
# -----------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# -----------------------------
# JWT Configuration
# -----------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}

# -----------------------------
# URL Configuration
# -----------------------------
ROOT_URLCONF = 'backend_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_django.wsgi.application'

# -----------------------------
# Database
# -----------------------------
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# -----------------------------
# Authentication
# -----------------------------
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
AUTH_USER_MODEL = 'accounts.User'

# -----------------------------
# Password Validation
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# -----------------------------
# Internationalization
# -----------------------------
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# Static Files
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------
# Media Files (Cloudinary)
# -----------------------------
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config("CLOUD_NAME", default="").strip(),
    'API_KEY': config("CLOUD_API_KEY", default="").strip(),
    'API_SECRET': config("CLOUD_API_SECRET", default="").strip(),
}

# Configure cloudinary si les credentials sont présents
if all([CLOUDINARY_STORAGE['CLOUD_NAME'], 
        CLOUDINARY_STORAGE['API_KEY'], 
        CLOUDINARY_STORAGE['API_SECRET']]):
    try:
        import cloudinary
        import cloudinary.uploader
        import cloudinary.api
        
        cloudinary.config(
            cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
            api_key=CLOUDINARY_STORAGE['API_KEY'],
            api_secret=CLOUDINARY_STORAGE['API_SECRET'],
            secure=True
        )
    except ImportError:
        pass
else:
    if not DEBUG:
        import warnings
        warnings.warn(
            " Cloudinary non configuré. L'upload d'images ne fonctionnera pas.",
            RuntimeWarning
        )

# -----------------------------
# Default Primary Key Field Type
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------
# Security Settings (Production)
# -----------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True




