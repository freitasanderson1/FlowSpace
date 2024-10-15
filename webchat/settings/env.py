from webchat.settings.base import *

SECRET_KEY = '@2#kh+^qzs+dsrw37rv@hp$+7vu51u(827mcnf1$rbqiz(+1qq'

DEBUG = True

ALLOWED_HOSTS=['localhost','127.0.0.1','0.0.0.0']

CSRF_TRUSTED_ORIGINS = ['http://localhost:3357', 'http://localhost:3357']

CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}