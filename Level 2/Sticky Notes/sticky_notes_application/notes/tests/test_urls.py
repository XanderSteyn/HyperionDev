"""
Unit tests for URL patterns in the sticky notes application
Covers correct URL resolution for all note views
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.urls import reverse, resolve


class NoteURLTest(TestCase):
    """
    Test cases for URL patterns in the notes app
    Verifies correct URL resolution for each view
    """
    def test_note_list_url(self):
        """
        Test that note list URL resolves to the correct view
        """
        url = reverse("note_list")
        self.assertEqual(url, "/")
        resolver = resolve(url)
        # Should resolve to the note_list view function
        self.assertEqual(resolver.func.__name__, "note_list")

    def test_note_detail_url(self):
        """
        Test that note detail URL resolves to the correct view
        """
        url = reverse("note_detail", args=[1])
        self.assertEqual(url, "/note/1/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_detail")

    def test_note_create_url(self):
        """
        Test that note create URL resolves to the correct view
        """
        url = reverse("note_create")
        self.assertEqual(url, "/note/new/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_create")

    def test_note_update_url(self):
        """
        Test that note update URL resolves to the correct view
        """
        url = reverse("note_update", args=[1])
        self.assertEqual(url, "/note/1/edit/")
        resolver = resolve(url)
        # Should resolve to the note_update view function
        self.assertEqual(resolver.func.__name__, "note_update")

    def test_note_delete_url(self):
        """
        Test that note delete URL resolves to the correct view
        """
        url = reverse("note_delete", args=[1])
        self.assertEqual(url, "/note/1/delete/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_delete")
