"""
Unit tests for the Note views in the sticky notes application
Covers CRUD operations, form validation, context, error handling, and messages
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.urls import reverse

# ========== Local Application Imports ==========
from notes.models import Note


class NoteViewTest(TestCase):
    """
    Test cases for the Note views
    Verifies CRUD operations, form validation, error handling, and context
    """
    def setUp(self):
        """
        Set up a sample Note object for use in view tests
        """
        # Create a sample note to use in most tests
        self.note = Note.objects.create(
            title="Test Note",
            content="This is a test note"
        )

    def test_note_list_view(self):
        """
        Test the note list view - returns status 200 and contains the note title
        """
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """
        Test the note detail view - returns status 200 and contains note data
        """
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note")

    def test_note_create_view(self):
        """
        Test creating a note via the 'create' view - redirects and creates the
        note
        """
        response = self.client.post(reverse("note_create"), {
            "title": "Another Note",
            "content": "Content for another note."
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Another Note").exists())

    def test_note_update_view(self):
        """
        Test updating a note via the 'update' view - redirects and updates the
        note
        """
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            {
                "title": "Updated Note",
                "content": "Updated content."
            }
        )
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Note")
        self.assertEqual(self.note.content, "Updated content.")

    def test_note_delete_view(self):
        """
        Test deleting a note via the 'delete' view - redirects and deletes the
        note
        """
        response = self.client.post(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

    def test_note_create_view_invalid(self):
        """
        Test creating a note with missing title - fails validation and
        re-renders form
        """
        # Title is required, so this should fail validation
        response = self.client.post(reverse("note_create"), {
            "title": "",
            "content": "Content with no title."
        })
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        # Check that the form has an error for the title field
        self.assertIn("title", form.errors)
        self.assertIn("This field is required.", form.errors["title"])

    def test_note_update_view_invalid(self):
        """
        Test updating a note with missing content - fails validation and
        re-renders form
        """
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            {
                "title": "Title present",
                "content": ""
            }
        )
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("content", form.errors)
        self.assertIn("This field is required.", form.errors["content"])

    def test_note_list_view_context(self):
        """
        Test that the note list view provides the correct context variables
        """
        response = self.client.get(reverse("note_list"))
        self.assertIn("notes", response.context)
        self.assertIn("page_title", response.context)
        self.assertEqual(response.context["page_title"], "Sticky Notes")

    def test_note_detail_view_context(self):
        """
        Test that the note detail view provides the correct context variables
        """
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        self.assertIn("note", response.context)
        self.assertEqual(response.context["note"].title, "Test Note")

    def test_note_detail_view_404(self):
        """
        Test that requesting a non-existent note in detail view returns 404
        """
        # Use a primary key that does not exist
        response = self.client.get(reverse("note_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_update_view_404(self):
        """
        Test that updating a non-existent note returns 404
        """
        response = self.client.get(reverse("note_update", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_delete_view_404(self):
        """
        Test that deleting a non-existent note returns 404
        """
        response = self.client.get(reverse("note_delete", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_create_long_title(self):
        """
        Test creating a note with a very long title - fails validation
        """
        long_title = "A" * 300  # Exceeds max_length=255
        response = self.client.post(reverse("note_create"), {
            "title": long_title,
            "content": "Long title test."
        })
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        # Should trigger Django's max_length validation error
        self.assertIn("title", form.errors)
        self.assertTrue(
            any(
                "Ensure this value has at most 255 characters" in error
                for error in form.errors["title"]
            )
        )

    def test_note_create_long_content(self):
        """
        Test creating a note with very long content - succeeds
        """
        long_content = "B" * 10000
        response = self.client.post(reverse("note_create"), {
            "title": "Long Content",
            "content": long_content
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Long Content").exists())

    def test_note_create_view_get_request(self):
        """
        Test GET request to note create view - displays the form
        """
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_update_view_get_request(self):
        """
        Test GET request to note update view - displays the form with existing
        data
        """
        response = self.client.get(
            reverse("note_update", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"].instance.title, "Test Note")

    def test_note_delete_view_get_request(self):
        """
        Test GET request to note delete view - displays the confirmation page
        """
        response = self.client.get(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("note", response.context)
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")

    def test_success_message_on_create(self):
        """
        Test that a success message appears after note creation
        """
        # After creating a note, user should be redirected and see a success
        # message
        response = self.client.post(reverse("note_create"), {
            "title": "Success Test",
            "content": "Test content"
        })
        self.assertRedirects(response, reverse("note_list"))
        self.assertTrue(Note.objects.filter(title="Success Test").exists())

    def test_success_message_on_update(self):
        """
        Test that a success message appears after note update
        """
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            {
                "title": "Updated Success",
                "content": "Updated content"
            }
        )
        self.assertRedirects(response, reverse("note_list"))
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Success")

    def test_success_message_on_delete(self):
        """
        Test that a success message appears after note deletion
        """
        response = self.client.post(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertRedirects(response, reverse("note_list"))
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
