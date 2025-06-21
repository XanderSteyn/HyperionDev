"""
Main URL configuration for the sticky notes application

This file defines the top-level URL patterns for the entire application
It includes the Django admin interface and delegates all other URLs
to the notes application for handling sticky note functionality

The URL structure follows RESTful conventions with clear, descriptive
paths for different operations on sticky notes
"""

# ============= Third-Party Imports =============
from django.contrib import admin
from django.urls import path, include

# Main URL patterns for the sticky notes application
urlpatterns = [
    # Django admin interface - accessible at /admin/
    path("admin/", admin.site.urls),

    # Include all URLs from the notes application
    # All sticky note functionality is handled by the notes app
    path("", include("notes.urls")),
]
