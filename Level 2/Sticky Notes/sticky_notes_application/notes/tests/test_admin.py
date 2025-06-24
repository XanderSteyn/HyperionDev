"""
Unit tests for the Note admin interface in the sticky notes application
Covers admin list display, search, filters, readonly fields, and content
preview
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.contrib import admin

# ========== Local Application Imports ==========
from notes.models import Note
from notes.admin import NoteAdmin


class NoteAdminTest(TestCase):
    """
    Test cases for the Note admin interface
    Verifies admin list display, search, filters, readonly fields, and content
    preview
    """
    def setUp(self):
        """
        Set up sample Note objects for use in admin tests
        """
        # Create two notes: one with short content, one with long content
        self.note1 = Note.objects.create(
            title="Short Note",
            content="Short content"
        )
        self.note2 = Note.objects.create(
            title="Long Note",
            content="A" * 150
        )

    def test_admin_content_preview_short(self):
        """
        Test admin content preview for short content - shows full content
        """
        admin_instance = NoteAdmin(Note, admin.site)
        preview = admin_instance.content_preview(self.note1)
        self.assertEqual(preview, "Short content")

    def test_admin_content_preview_long(self):
        """
        Test admin content preview for long content - is truncated
        """
        admin_instance = NoteAdmin(Note, admin.site)
        preview = admin_instance.content_preview(self.note2)
        # Should end with '...' and be 103 chars (100 + '...')
        self.assertIn("...", preview)
        self.assertEqual(len(preview), 103)  # 100 chars + '...'

    def test_admin_list_display(self):
        """
        Test admin list display configuration - includes expected fields
        """
        admin_instance = NoteAdmin(Note, admin.site)
        # Should display title, content preview, and created_at in admin list
        self.assertIn("title", admin_instance.list_display)
        self.assertIn("content_preview", admin_instance.list_display)
        self.assertIn("created_at", admin_instance.list_display)

    def test_admin_search_fields(self):
        """
        Test admin search fields configuration - includes title and content
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("title", admin_instance.search_fields)
        self.assertIn("content", admin_instance.search_fields)

    def test_admin_list_filter(self):
        """
        Test admin list filter configuration - includes created_at
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("created_at", admin_instance.list_filter)

    def test_admin_readonly_fields(self):
        """
        Test admin readonly fields configuration - includes created_at
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("created_at", admin_instance.readonly_fields)

    def test_admin_ordering(self):
        """
        Test admin ordering configuration - is set to -created_at
        """
        admin_instance = NoteAdmin(Note, admin.site)
        # Notes should be ordered newest first in admin
        self.assertEqual(admin_instance.ordering, ("-created_at",))
