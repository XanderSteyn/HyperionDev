"""
URL patterns for the sticky notes application

This module defines all the URL patterns that map web addresses to
view functions in the sticky notes application. It implements a
RESTful URL structure with clear, descriptive paths for different
operations on sticky notes

The URL patterns follow Django's path() function syntax and include
named URL patterns for easy reverse lookup in templates and views
"""

# ============= Third-Party Imports =============
from django.urls import path

# ========== Local Application Imports ==========
from .views import (
    note_list,
    note_detail,
    note_create,
    note_update,
    note_delete
)

# Each pattern maps a URL path to a specific view function
urlpatterns = [
    # Main page - displays all notes in a list
    path("", note_list, name="note_list"),

    # Individual note view - shows full details of a specific note
    path("note/<int:pk>/", note_detail, name="note_detail"),

    # Create new note - displays form for creating a new note
    path("note/new/", note_create, name="note_create"),

    # Edit existing note - displays form pre-filled with note data
    path("note/<int:pk>/edit/", note_update, name="note_update"),

    # Delete note - displays confirmation page for note deletion
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
]
