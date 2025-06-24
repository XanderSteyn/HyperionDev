"""
ASGI configuration for the sticky notes application

This module exposes the ASGI callable as a module-level variable named
'application'. ASGI (Asynchronous Server Gateway Interface) is a
specification that allows web servers to communicate with Python web
applications using async/await syntax

This enables deployment on modern async web servers and supports WebSocket
connections if needed in the future. ASGI is the successor to WSGI and
provides better performance for concurrent connections
"""

# =========== Standard Library Imports ==========
import os

# ============= Third-Party Imports =============
from django.core.asgi import get_asgi_application

# Set the Django settings module for the ASGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sticky_notes.settings")

# Create the ASGI application object
application = get_asgi_application()
