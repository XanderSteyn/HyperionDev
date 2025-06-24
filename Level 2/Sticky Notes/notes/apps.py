"""
Application configuration for the sticky notes application

This module defines the application configuration class that Django
uses to manage the sticky notes app. It contains metadata about the
app and configuration settings that are loaded when the app is
installed in INSTALLED_APPS

The configuration includes settings for the default auto field type
and the application name that Django uses for internal references
"""

# ============= Third-Party Imports =============
from django.apps import AppConfig


class NotesConfig(AppConfig):
    """
    Configuration class for the sticky notes application

    Defines the app's metadata and configuration settings including
    the app name and default auto field type for database primary keys
    This configuration is automatically loaded by Django when the app
    is installed in INSTALLED_APPS
    """
    # Set the default field type for auto-generated primary keys
    default_auto_field = "django.db.models.BigAutoField"

    # Define the internal Django name for the app
    name = "notes"
