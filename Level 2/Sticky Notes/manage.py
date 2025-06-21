"""
Django management script for the sticky notes application

This script provides command-line access to Django's management commands
for the sticky notes application. It handles tasks like running the development
server, creating database migrations, collecting static files, and more

Usage examples:
- python manage.py runserver        # Start development server
- python manage.py makemigrations   # Create database migrations
- python manage.py migrate          # Apply database migrations
- python manage.py collectstatic    # Collect static files
- python manage.py createsuperuser  # Create admin user
"""

# =========== Standard Library Imports ==========
import os
import sys


def main():
    """
    Execute Django management commands for the sticky notes application

    Sets up the Django environment and executes the requested management
    command. Handles import errors with helpful error messages for common
    setup issues
    """
    # Set the default settings module for the Django project
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sticky_notes.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as error:
        raise ImportError(
            "Couldn't import Django! Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from error
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    # Ensure the main function is called only when the script is
    # executed directly
    main()
