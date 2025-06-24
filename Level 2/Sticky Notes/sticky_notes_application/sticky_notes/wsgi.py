"""
WSGI configuration for the sticky notes application

This module exposes the WSGI callable as a module-level variable named
'application'. WSGI (Web Server Gateway Interface) is a specification
that allows web servers to communicate with Python web applications

This enables deployment on traditional web servers like Apache or Nginx
using WSGI-compatible servers like Gunicorn or uWSGI
"""

# =========== Standard Library Imports ==========
import os

# ============= Third-Party Imports =============
from django.core.wsgi import get_wsgi_application

# Set the Django settings module for the WSGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sticky_notes.settings")

# Create the WSGI application object
application = get_wsgi_application()
