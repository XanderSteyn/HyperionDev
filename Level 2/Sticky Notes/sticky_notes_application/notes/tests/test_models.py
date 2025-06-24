"""
Unit tests for the Note model and its methods in the sticky notes application
Covers model field validation, creation, and string representation
"""

# ============= Third-Party Imports =============
from django.test import TestCase

# ========== Local Application Imports ==========
from notes.models import Note


class NoteModelTest(TestCase):
    """
    Test cases for the Note model
    Verifies field validation, creation, and __str__ method
    """
    def setUp(self):
        """
        Set up a sample Note object for use in tests
        """
        # Create a sample note for model tests
        Note.objects.create(title="Test Note", content="This is a test note")

    def test_note_has_title(self):
        """
        Test that the Note object has the expected title
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        """
        Test that the Note object has the expected content
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note")

    def test_note_created_at_field(self):
        """
        Test that the created_at field is automatically set
        """
        note = Note.objects.get(id=1)
        # created_at should be set by auto_now_add
        self.assertIsNotNone(note.created_at)

    def test_note_model_str_representation(self):
        """
        Test the string representation (__str__) of the Note model
        """
        note = Note.objects.get(id=1)
        # __str__ should return the note's title
        self.assertEqual(str(note), "Test Note")


class NoteModelMethodTest(TestCase):
    """
    Test cases for Note model methods, including __str__
    """
    def test_note_str_method(self):
        """
        Test the __str__ method - returns the note title
        """
        note = Note.objects.create(title="String Method", content="Test")
        # __str__ should return the title for any note
        self.assertEqual(str(note), "String Method")
