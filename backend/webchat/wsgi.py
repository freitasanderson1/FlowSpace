import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webchat.settings')

print("WSGI application is being used.")

application = get_wsgi_application()
