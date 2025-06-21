"""
Admin interface configuration for the sticky notes application

This module configures the Django admin interface for managing sticky
notes. It provides an admin interface with enhanced features like search,
filtering, and content previews

The admin interface allows administrators to perform CRUD operations
on notes through a web interface with proper validation and data management
capabilities
"""

# ============= Third-Party Imports =============
from django.contrib import admin

# ========== Local Application Imports ==========
from .models import Note


# Admin interface registration for the Note model
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for managing sticky notes

    Provides an admin interface for note management with:
    - List view showing title, content preview, and creation date
    - Search functionality across title and content fields
    - Date-based filtering for easy note discovery
    - Read-only creation timestamp to prevent modification
    - Reverse chronological ordering (newest first)
    """

    # Fields to display in the admin list view
    list_display = ('title', 'content_preview', 'created_at')

    # Sidebar filters for date-based filtering
    list_filter = ('created_at',)

    # Enable search by title or content
    search_fields = ('title', 'content')

    # Make creation time read-only to prevent edits
    readonly_fields = ('created_at',)

    # Order notes from newest to oldest
    ordering = ('-created_at',)

    def content_preview(self, obj):
        """
        Generate a truncated preview of note content for admin list display

        Arguments:
            obj (Note): The Note instance being displayed

        Returns:
            str: Truncated content preview (first 100 characters, with
                                           ellipsis if longer)
        """
        return (
            obj.content[:100] + '...'
            if len(obj.content) > 100 else obj.content
        )

    # Label for the custom content preview column
    content_preview.short_description = 'Content Preview'
