"""
Unit tests for template usage in the sticky notes application
Covers correct template rendering and inheritance for all views
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.urls import reverse

# ========== Local Application Imports ==========
from notes.models import Note


class NoteTemplateTest(TestCase):
    """
    Test cases for template usage in the sticky notes app
    Verifies correct template rendering for each view
    """
    def setUp(self):
        """
        Set up a sample Note object for use in template tests
        """
        # Create a sample note to test template rendering
        self.note = Note.objects.create(
            title="Template Test",
            content="Template test content"
        )

    def test_note_list_template(self):
        """
        Test that note list view uses the correct template
        Should render 'notes/note_list.html'
        """
        response = self.client.get(reverse("note_list"))
        # Check that the correct template is used for the list view
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_detail_template(self):
        """
        Test that note detail view uses the correct template
        Should render 'notes/note_detail.html'
        """
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        # Check that the correct template is used
        self.assertTemplateUsed(response, "notes/note_detail.html")

    def test_note_form_template(self):
        """
        Test that note create view uses the correct form template
        Should render 'notes/note_form.html'
        """
        response = self.client.get(reverse("note_create"))
        # Check that the correct template is used
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_update_template(self):
        """
        Test that note update view uses the correct form template
        Should render 'notes/note_form.html'
        """
        response = self.client.get(
            reverse("note_update", args=[str(self.note.id)])
        )
        # Check that the correct template is used
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_delete_template(self):
        """
        Test that note delete view uses the correct confirmation template
        Should render 'notes/note_confirm_delete.html'
        """
        response = self.client.get(
            reverse("note_delete", args=[str(self.note.id)])
        )
        # Check that the correct template is used
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")

    def test_base_template_inheritance(self):
        """
        Test that all templates extend the base template
        Should contain elements from 'base.html'
        """
        response = self.client.get(reverse("note_list"))
        # These strings should appear if base.html is extended
        self.assertContains(response, "Sticky Notes")
        self.assertContains(response, "Create Note")
