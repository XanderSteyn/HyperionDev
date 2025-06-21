"""
Tests for the sticky notes application

This module contains unit tests for the sticky notes application, covering all
aspects of the application including models, views, forms, and edge cases
The tests ensure the application functions correctly and handles various
scenarios including validation, error cases, and user interactions

The tests use Django's TestCase class and follow best practices for testing
Django applications, including proper setup, teardown, and assertion methods
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.urls import reverse

# ========== Local Application Imports ==========
from .models import Note


class NoteModelTest(TestCase):
    """
    Test cases for the Note model

    This test class verifies that the Note model functions correctly,
    including field validation, model creation, and the __str__ method
    Tests ensure that notes can be created with proper data and that
    the model behaves as expected in various scenarios
    """

    def setUp(self):
        """
        Set up test data for each test method

        Creates:
            Note: A test note with title 'Test Note' and content
                  'This is a test note'
        """
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note')

    def test_note_has_title(self):
        """
        Test that a Note object has the expected title

        Returns:
            None: Test passes if the note title matches expected value
        """
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        """
        Test that a Note object has the expected content

        Returns:
            None: Test passes if the note content matches expected value
        """
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note')


class NoteViewTest(TestCase):
    """
    Test cases for the Note views

    This test class verifies that all view functions work correctly,
    including CRUD operations, form validation, error handling, and
    edge cases. Tests cover both successful operations and error
    scenarios to ensure robust application behavior
    """

    def setUp(self):
        """
        Set up test data for view testing

        Creates:
            Note: A test note with title 'Test Note' and content
                  'This is a test note' stored in self.note
        """
        # Create a Note object for testing views
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note'
        )

    def test_note_list_view(self):
        """
        Test the note list view functionality

        Returns:
            None: Test passes if response status is 200 and contains note title
        """
        # Test the note-list view
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        """
        Test the note detail view functionality

        Returns:
            None: Test passes if response status is 200 and contains note data
        """
        # Test the note-detail view
        response = self.client.get(
            reverse('note_detail', args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note')

    def test_note_create_view(self):
        """
        Test note creation functionality

        Returns:
            None: Test passes if note is created and response redirects
        """
        # Test the note-create view
        response = self.client.post(reverse('note_create'), {
            'title': 'Another Note',
            'content': 'Content for another note.'
        })
        # Should redirect after creation
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title='Another Note').exists())

    def test_note_update_view(self):
        """
        Test note update functionality

        Returns:
            None: Test passes if note is updated and response redirects
        """
        # Test the note-update view
        response = self.client.post(
            reverse('note_update', args=[str(self.note.id)]),
            {
                'title': 'Updated Note',
                'content': 'Updated content.'
            }
        )
        # Should redirect after update
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')
        self.assertEqual(self.note.content, 'Updated content.')

    def test_note_delete_view(self):
        """
        Test note deletion functionality

        Returns:
            None: Test passes if note is deleted and response redirects
        """
        # Test the note-delete view
        response = self.client.post(
            reverse('note_delete', args=[str(self.note.id)])
        )
        # Should redirect after delete
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())

    def test_note_create_view_invalid(self):
        """
        Test form validation for note creation

        Returns:
            None: Test passes if form validation works correctly
        """
        # Test creating a note with missing title (should fail validation)
        response = self.client.post(reverse('note_create'), {
            'title': '',
            'content': 'Content with no title.'
        })
        self.assertEqual(response.status_code, 200)  # Form re-renders
        form = response.context['form']
        self.assertIn('title', form.errors)
        self.assertIn('This field is required.', form.errors['title'])

    def test_note_update_view_invalid(self):
        """
        Test form validation for note updates

        Returns:
            None: Test passes if form validation works correctly
        """
        # Test updating a note with missing content (should fail validation)
        response = self.client.post(
            reverse('note_update', args=[str(self.note.id)]),
            {
                'title': 'Title present',
                'content': ''
            }
        )
        self.assertEqual(response.status_code, 200)  # Form re-renders
        form = response.context['form']
        self.assertIn('content', form.errors)
        self.assertIn('This field is required.', form.errors['content'])

    def test_note_list_view_context(self):
        """
        Test context variables in the note list view

        Returns:
            None: Test passes if context contains expected variables
        """
        # Test that the note_list view provides the correct context
        response = self.client.get(reverse('note_list'))
        self.assertIn('notes', response.context)
        self.assertIn('page_title', response.context)
        self.assertEqual(response.context['page_title'], 'Sticky Notes')

    def test_note_detail_view_context(self):
        """
        Test context variables in the note detail view

        Returns:
            None: Test passes if context contains expected variables
        """
        # Test that the note_detail view provides the correct context
        response = self.client.get(
            reverse('note_detail', args=[str(self.note.id)])
        )
        self.assertIn('note', response.context)
        self.assertEqual(response.context['note'].title, 'Test Note')

    def test_note_detail_view_404(self):
        """
        Test 404 error handling for non-existent notes in detail view

        Returns:
            None: Test passes if 404 error is returned
        """
        # Test that requesting a non-existent note returns 404
        response = self.client.get(reverse('note_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_update_view_404(self):
        """
        Test 404 error handling for non-existent notes in update view

        Returns:
            None: Test passes if 404 error is returned
        """
        # Test that updating a non-existent note returns 404
        response = self.client.get(reverse('note_update', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_delete_view_404(self):
        """
        Test 404 error handling for non-existent notes in delete view

        Returns:
            None: Test passes if 404 error is returned
        """
        # Test that deleting a non-existent note returns 404
        response = self.client.get(reverse('note_delete', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_create_long_title(self):
        """
        Test title length validation in note creation

        Returns:
            None: Test passes if title length validation works correctly
        """
        # Test creating a note with a very long title (over 255 chars)
        long_title = 'A' * 300
        response = self.client.post(reverse('note_create'), {
            'title': long_title,
            'content': 'Long title test.'
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIn('title', form.errors)
        self.assertTrue(
            any(
                'Ensure this value has at most 255 characters' in error
                for error in form.errors['title']
            )
        )

    def test_note_create_long_content(self):
        """
        Test content length handling in note creation

        Returns:
            None: Test passes if long content is handled correctly
        """
        # Test creating a note with a very long content (should succeed)
        long_content = 'B' * 10000
        response = self.client.post(reverse('note_create'), {
            'title': 'Long Content',
            'content': long_content
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title='Long Content').exists())


class NoteModelMethodTest(TestCase):
    """
    Test cases for Note model methods

    This test class verifies that specific methods of the Note model
    work correctly, including the __str__ method and any other custom
    methods that may be added to the model

    Test Methods:
        test_note_str_method: Tests the __str__ method of the Note model
    """

    def test_note_str_method(self):
        """
        Test the __str__ method of the Note model

        Returns:
            None: Test passes if __str__ returns the note title
        """
        note = Note.objects.create(title='String Method', content='Test')
        self.assertEqual(str(note), 'String Method')
