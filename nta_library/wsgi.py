"""
WSGI config for nta_library project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django_forest import init_forest


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nta_library.settings')

application = get_wsgi_application()

init_forest()
application = get_wsgi_application()

