"""
Unit tests for edge cases and error scenarios in the sticky notes application
Covers empty lists, special characters, unicode, and HTML content
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.urls import reverse

# ========== Local Application Imports ==========
from notes.models import Note


class NoteEdgeCaseTest(TestCase):
    """
    Test cases for edge cases and error scenarios in notes
    Verifies handling of empty lists, special characters, unicode, and
    HTML content
    """
    def test_empty_note_list(self):
        """
        Test behavior when no notes exist (empty state)
        """
        response = self.client.get(reverse("note_list"))
        # Should not contain any note titles since the DB is empty
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Test Note")

    def test_note_with_special_characters(self):
        """
        Test note creation with special characters in title and content
        """
        response = self.client.post(reverse("note_create"), {
            'title': "Special & Characters < > \" '",
            'content': "Content with special chars: & < > \" '"
        })
        self.assertEqual(response.status_code, 302)
        # Ensure special characters are saved and retrievable
        note = Note.objects.get(title="Special & Characters < > \" '")
        self.assertIn('& < > " \'', note.content)

    def test_note_with_unicode_characters(self):
        """
        Test note creation with unicode (Chinese) characters in title and
        content
        """
        unicode_str = "测试"  # "test" in Chinese
        response = self.client.post(reverse("note_create"), {
            "title": f"Unicode: {unicode_str}",
            "content": f"Content with unicode: {unicode_str}"
        })
        self.assertEqual(response.status_code, 302)
        # Ensure unicode is saved and retrievable
        note = Note.objects.get(title=f"Unicode: {unicode_str}")
        self.assertIn(unicode_str, note.content)

    def test_note_with_html_content(self):
        """
        Test note creation with HTML content in the note body
        """
        response = self.client.post(reverse("note_create"), {
            "title": "HTML Test",
            "content": "<script>alert('test')</script><p>Hello</p>"
        })
        self.assertEqual(response.status_code, 302)
        # Ensure HTML is saved as raw text in the DB
        note = Note.objects.get(title="HTML Test")
        self.assertIn("<script>alert('test')</script>", note.content)
