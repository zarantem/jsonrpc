"""
WSGI config for jsonrpc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jsonrpc.settings')

WSGI_APPLICATION = 'mysite.wsgi.application'
WSGI_SSL_CERTIFICATE = os.getenv('cert')
WSGI_SSL_PRIVATE_KEY = os.getenv('key')

