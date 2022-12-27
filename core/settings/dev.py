from .base import *

from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_POSTGRES_DB'),
        'USER': os.getenv('DJANGO_POSTGRES_USER'),
        'PASSWORD': os.getenv('DJANGO_POSTGRES_DB_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}

# django rest framework simplejwt configurations
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'SIGNING_KEY': os.getenv('JWT_SECRET'),
}