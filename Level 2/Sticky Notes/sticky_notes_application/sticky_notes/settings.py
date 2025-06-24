"""
Django settings for the sticky notes application

This configuration file contains all the settings needed to run the sticky
notes web application. It includes database configuration, installed apps,
middleware settings, static file handling, and security settings

For development purposes, this uses a SQLite database and debug mode is enabled
For production deployment, these settings should be adjusted for security,
for example, disable 'DEBUG' and load the 'SECRET_KEY' from an environment
variable
"""

# =========== Standard Library Imports ==========
from pathlib import Path

# Build paths inside the application like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# Security Warning: Keep the secret key used in production secret
# It is used for cryptographic signing (sessions, cookies, tokens)
# This key should be stored in an environment variable in production
SECRET_KEY = (
    "django-insecure-=i&9lj@#_35nr7yw*gh56%ejuh0e^7_trad9s=((lmwd@auxyy"
)

# DEBUG enables detailed error pages and auto-reloading during development
# It exposes sensitive information and should always be set to False in
# production
DEBUG = True

# Hosts that can serve this Django application
# Empty list means only localhost can serve the app
ALLOWED_HOSTS = []

# List of Django applications that are enabled in this application
INSTALLED_APPS = [
    "django.contrib.admin",         # Django's automatic admin interface
    "django.contrib.auth",          # Authentication system
    "django.contrib.contenttypes",  # Framework for content types
    "django.contrib.sessions",      # Session framework
    "django.contrib.messages",      # Messaging framework
    "django.contrib.staticfiles",   # Static file handling
    # Custom Applications
    "notes",                        # Sticky notes application
]

# Middleware classes that process requests and responses
# Order matters - middleware is processed in the order listed
MIDDLEWARE = [
    # Security enhancements
    "django.middleware.security.SecurityMiddleware",
    # Session handling
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Common functionality
    "django.middleware.common.CommonMiddleware",
    # CSRF protection
    "django.middleware.csrf.CsrfViewMiddleware",
    # User authentication
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Message handling
    "django.contrib.messages.middleware.MessageMiddleware",
    # Clickjacking protection
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL configuration for the application
ROOT_URLCONF = "sticky_notes.urls"

# Defines how Django processes and renders HTML templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = "sticky_notes.wsgi.application"

# SQLite database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Configure language and timezone for the application
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True

# Static files configuration (CSS, JavaScript, Images)
# Handles serving of static assets like stylesheets and scripts
STATIC_URL = "static/"

# Additional directories where Django looks for static files
STATICFILES_DIRS = [
    BASE_DIR / "notes/static",
]

# Directory where collectstatic command will gather all static files
STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type for models
# Uses BigAutoField for better performance with large datasets
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
