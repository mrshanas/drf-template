from .base import *

DEBUG = False

# In production, the browsable API is disabled using the renderer class
REST_FRAMWORK = {}

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_POSTGRES_DB'),
        'USER': os.getenv('DJANGO_POSTGRES_USER'),
        'PASSWORD': os.getenv('DJANGO_POSTGRES_DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}