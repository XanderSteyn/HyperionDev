"""
Tests for the sticky notes application

This module contains unit tests for the sticky notes application, covering all
aspects of the application including models, views, forms, admin, URLs,
templates, messages, and edge cases
The tests ensure the application functions correctly and handles various
scenarios including validation, error cases, and user interactions

The tests use Django's TestCase class and follow best practices for testing
Django applications, including proper setup, teardown, and assertion methods
"""

# ============= Third-Party Imports =============
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib import admin

# ========== Local Application Imports ==========
from .models import Note
from .admin import NoteAdmin


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
        Note.objects.create(title="Test Note", content="This is a test note")

    def test_note_has_title(self):
        """
        Test that a Note object has the expected title

        Returns:
            None: Test passes if the note title matches expected value
        """
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        """
        Test that a Note object has the expected content

        Returns:
            None: Test passes if the note content matches expected value
        """
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note")

    def test_note_created_at_field(self):
        """
        Test that the created_at field is automatically set

        Returns:
            None: Test passes if created_at field is not None
        """
        note = Note.objects.get(id=1)
        self.assertIsNotNone(note.created_at)

    def test_note_model_str_representation(self):
        """
        Test the string representation of the Note model

        Returns:
            None: Test passes if __str__ returns the note title
        """
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), "Test Note")


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
            title="Test Note",
            content="This is a test note"
        )

    def test_note_list_view(self):
        """
        Test the note list view functionality

        Returns:
            None: Test passes if response status is 200 and contains note title
        """
        # Test the note-list view
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """
        Test the note detail view functionality

        Returns:
            None: Test passes if response status is 200 and contains note data
        """
        # Test the note-detail view
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note")

    def test_note_create_view(self):
        """
        Test note creation functionality

        Returns:
            None: Test passes if note is created and response redirects
        """
        # Test the note-create view
        response = self.client.post(reverse("note_create"), {
            "title": "Another Note",
            "content": "Content for another note."
        })
        # Should redirect after creation
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Another Note").exists())

    def test_note_update_view(self):
        """
        Test note update functionality

        Returns:
            None: Test passes if note is updated and response redirects
        """
        # Test the note-update view
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            {
                "title": "Updated Note",
                "content": "Updated content."
            }
        )
        # Should redirect after update
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Note")
        self.assertEqual(self.note.content, "Updated content.")

    def test_note_delete_view(self):
        """
        Test note deletion functionality

        Returns:
            None: Test passes if note is deleted and response redirects
        """
        # Test the note-delete view
        response = self.client.post(
            reverse("note_delete", args=[str(self.note.id)])
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
        response = self.client.post(reverse("note_create"), {
            "title": "",
            "content": "Content with no title."
        })
        self.assertEqual(response.status_code, 200)  # Form re-renders
        form = response.context["form"]
        self.assertIn("title", form.errors)
        self.assertIn("This field is required.", form.errors["title"])

    def test_note_update_view_invalid(self):
        """
        Test form validation for note updates

        Returns:
            None: Test passes if form validation works correctly
        """
        # Test updating a note with missing content (should fail validation)
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            {
                "title": "Title present",
                "content": ""
            }
        )
        self.assertEqual(response.status_code, 200)  # Form re-renders
        form = response.context["form"]
        self.assertIn("content", form.errors)
        self.assertIn("This field is required.", form.errors["content"])

    def test_note_list_view_context(self):
        """
        Test context variables in the note list view

        Returns:
            None: Test passes if context contains expected variables
        """
        # Test that the note_list view provides the correct context
        response = self.client.get(reverse("note_list"))
        self.assertIn("notes", response.context)
        self.assertIn("page_title", response.context)
        self.assertEqual(response.context["page_title"], "Sticky Notes")

    def test_note_detail_view_context(self):
        """
        Test context variables in the note detail view

        Returns:
            None: Test passes if context contains expected variables
        """
        # Test that the note_detail view provides the correct context
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        self.assertIn("note", response.context)
        self.assertEqual(response.context["note"].title, "Test Note")

    def test_note_detail_view_404(self):
        """
        Test 404 error handling for non-existent notes in detail view

        Returns:
            None: Test passes if 404 error is returned
        """
        # Test that requesting a non-existent note returns 404
        response = self.client.get(reverse("note_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_update_view_404(self):
        """
        Test 404 error handling for non-existent notes in update view

        Returns:
            None: Test passes if 404 error is returned
        """
        # Test that updating a non-existent note returns 404
        response = self.client.get(reverse("note_update", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_delete_view_404(self):
        """
        Test 404 error handling for non-existent notes in delete view

        Returns:
            None: Test passes if 404 error is returned
        """
        # Test that deleting a non-existent note returns 404
        response = self.client.get(reverse("note_delete", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_note_create_long_title(self):
        """
        Test title length validation in note creation

        Returns:
            None: Test passes if title length validation works correctly
        """
        # Test creating a note with a very long title (over 255 chars)
        long_title = "A" * 300
        response = self.client.post(reverse("note_create"), {
            "title": long_title,
            "content": "Long title test."
        })
        self.assertEqual(response.status_code, 200)
        form = response.context["form"]
        self.assertIn("title", form.errors)
        self.assertTrue(
            any(
                "Ensure this value has at most 255 characters" in error
                for error in form.errors["title"]
            )
        )

    def test_note_create_long_content(self):
        """
        Test content length handling in note creation

        Returns:
            None: Test passes if long content is handled correctly
        """
        # Test creating a note with very long content (should succeed)
        long_content = "B" * 10000
        response = self.client.post(reverse("note_create"), {
            "title": "Long Content",
            "content": long_content
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Note.objects.filter(title="Long Content").exists())

    def test_note_create_view_get_request(self):
        """
        Test GET request to note create view

        Returns:
            None: Test passes if form is displayed correctly
        """
        response = self.client.get(reverse("note_create"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_update_view_get_request(self):
        """
        Test GET request to note update view

        Returns:
            None: Test passes if form is displayed with existing data
        """
        response = self.client.get(
            reverse("note_update", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertEqual(response.context["form"].instance.title, "Test Note")

    def test_note_delete_view_get_request(self):
        """
        Test GET request to note delete view

        Returns:
            None: Test passes if confirmation page is displayed
        """
        response = self.client.get(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("note", response.context)
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")

    def test_success_message_on_create(self):
        """
        Test success message appears after note creation

        Returns:
            None: Test passes if success message is displayed
        """
        response = self.client.post(reverse("note_create"), {
            "title": "Success Test",
            "content": "Test content"
        })
        self.assertRedirects(response, reverse("note_list"))
        # Verify the note was actually created
        self.assertTrue(Note.objects.filter(title="Success Test").exists())

    def test_success_message_on_update(self):
        """
        Test success message appears after note update

        Returns:
            None: Test passes if success message is displayed
        """
        response = self.client.post(
            reverse("note_update", args=[str(self.note.id)]),
            {
                "title": "Updated Success",
                "content": "Updated content"
            }
        )
        self.assertRedirects(response, reverse("note_list"))
        # Verify the note was actually updated
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated Success")

    def test_success_message_on_delete(self):
        """
        Test success message appears after note deletion

        Returns:
            None: Test passes if success message is displayed
        """
        response = self.client.post(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertRedirects(response, reverse("note_list"))
        # Verify the note was actually deleted
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())


class NoteURLTest(TestCase):
    """
    Test cases for URL patterns

    This test class verifies that all URL patterns are correctly configured
    and resolve to the appropriate views with the correct parameters
    """

    def test_note_list_url(self):
        """
        Test that note list URL resolves correctly

        Returns:
            None: Test passes if URL resolves to correct view
        """
        url = reverse("note_list")
        self.assertEqual(url, "/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_list")

    def test_note_detail_url(self):
        """
        Test that note detail URL resolves correctly

        Returns:
            None: Test passes if URL resolves to correct view
        """
        url = reverse("note_detail", args=[1])
        self.assertEqual(url, "/note/1/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_detail")

    def test_note_create_url(self):
        """
        Test that note create URL resolves correctly

        Returns:
            None: Test passes if URL resolves to correct view
        """
        url = reverse("note_create")
        self.assertEqual(url, "/note/new/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_create")

    def test_note_update_url(self):
        """
        Test that note update URL resolves correctly

        Returns:
            None: Test passes if URL resolves to correct view
        """
        url = reverse("note_update", args=[1])
        self.assertEqual(url, "/note/1/edit/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_update")

    def test_note_delete_url(self):
        """
        Test that note delete URL resolves correctly

        Returns:
            None: Test passes if URL resolves to correct view
        """
        url = reverse("note_delete", args=[1])
        self.assertEqual(url, "/note/1/delete/")
        resolver = resolve(url)
        self.assertEqual(resolver.func.__name__, "note_delete")


class NoteTemplateTest(TestCase):
    """
    Test cases for template usage

    This test class verifies that the correct templates are used
    for each view and that templates render correctly
    """

    def setUp(self):
        """
        Set up test data for template testing

        Creates:
            Note: A test note for template testing
        """
        self.note = Note.objects.create(
            title="Template Test",
            content="Template test content"
        )

    def test_note_list_template(self):
        """
        Test that note list view uses correct template

        Returns:
            None: Test passes if correct template is used
        """
        response = self.client.get(reverse("note_list"))
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_note_detail_template(self):
        """
        Test that note detail view uses correct template

        Returns:
            None: Test passes if correct template is used
        """
        response = self.client.get(
            reverse("note_detail", args=[str(self.note.id)])
        )
        self.assertTemplateUsed(response, "notes/note_detail.html")

    def test_note_form_template(self):
        """
        Test that note form view uses correct template

        Returns:
            None: Test passes if correct template is used
        """
        response = self.client.get(reverse("note_create"))
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_update_template(self):
        """
        Test that note update view uses correct template

        Returns:
            None: Test passes if correct template is used
        """
        response = self.client.get(
            reverse("note_update", args=[str(self.note.id)])
        )
        self.assertTemplateUsed(response, "notes/note_form.html")

    def test_note_delete_template(self):
        """
        Test that note delete view uses correct template

        Returns:
            None: Test passes if correct template is used
        """
        response = self.client.get(
            reverse("note_delete", args=[str(self.note.id)])
        )
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")

    def test_base_template_inheritance(self):
        """
        Test that all templates extend the base template

        Returns:
            None: Test passes if templates extend base.html
        """
        response = self.client.get(reverse("note_list"))
        self.assertContains(response, "Sticky Notes")
        self.assertContains(response, "Create Note")


class NoteAdminTest(TestCase):
    """
    Test cases for admin interface

    This test class verifies that the admin interface is correctly
    configured and functions as expected
    """

    def setUp(self):
        """
        Set up test data for admin testing

        Creates:
            Note: Test notes for admin testing
        """
        self.note1 = Note.objects.create(
            title="Short Note",
            content="Short content"
        )
        self.note2 = Note.objects.create(
            title="Long Note",
            content="A" * 150  # Long content to test preview
        )

    def test_admin_content_preview_short(self):
        """
        Test admin content preview for short content

        Returns:
            None: Test passes if preview shows full content
        """
        admin_instance = NoteAdmin(Note, admin.site)
        preview = admin_instance.content_preview(self.note1)
        self.assertEqual(preview, "Short content")

    def test_admin_content_preview_long(self):
        """
        Test admin content preview for long content

        Returns:
            None: Test passes if preview is truncated
        """
        admin_instance = NoteAdmin(Note, admin.site)
        preview = admin_instance.content_preview(self.note2)
        self.assertIn("...", preview)
        self.assertEqual(len(preview), 103)  # 100 chars + '...'

    def test_admin_list_display(self):
        """
        Test admin list display configuration

        Returns:
            None: Test passes if list display is configured correctly
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("title", admin_instance.list_display)
        self.assertIn("content_preview", admin_instance.list_display)
        self.assertIn("created_at", admin_instance.list_display)

    def test_admin_search_fields(self):
        """
        Test admin search fields configuration

        Returns:
            None: Test passes if search fields are configured correctly
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("title", admin_instance.search_fields)
        self.assertIn("content", admin_instance.search_fields)

    def test_admin_list_filter(self):
        """
        Test admin list filter configuration

        Returns:
            None: Test passes if list filter is configured correctly
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("created_at", admin_instance.list_filter)

    def test_admin_readonly_fields(self):
        """
        Test admin readonly fields configuration

        Returns:
            None: Test passes if readonly fields are configured correctly
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertIn("created_at", admin_instance.readonly_fields)

    def test_admin_ordering(self):
        """
        Test admin ordering configuration

        Returns:
            None: Test passes if ordering is configured correctly
        """
        admin_instance = NoteAdmin(Note, admin.site)
        self.assertEqual(admin_instance.ordering, ("-created_at",))


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
        note = Note.objects.create(title="String Method", content="Test")
        self.assertEqual(str(note), "String Method")


class NoteEdgeCaseTest(TestCase):
    """
    Test cases for edge cases and error scenarios

    This test class verifies that the application handles edge cases
    and error scenarios gracefully
    """

    def test_empty_note_list(self):
        """
        Test behavior when no notes exist

        Returns:
            None: Test passes if empty state is handled correctly
        """
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Test Note")

    def test_note_with_special_characters(self):
        """
        Test note creation with special characters

        Returns:
            None: Test passes if special characters are handled correctly
        """
        response = self.client.post(reverse("note_create"), {
            'title': 'Special & Characters < > " \'',
            'content': 'Content with special chars: & < > " \''
        })
        self.assertEqual(response.status_code, 302)
        note = Note.objects.get(title='Special & Characters < > " \'')
        self.assertIn('& < > " \'', note.content)

    def test_note_with_unicode_characters(self):
        """
        Test note creation with unicode characters

        Returns:
            None: Test passes if unicode characters are handled correctly
        """
        response = self.client.post(reverse("note_create"), {
            "title": "Unicode: 你好世界",
            "content": "Content with unicode: 你好世界"
        })
        self.assertEqual(response.status_code, 302)
        note = Note.objects.get(title="Unicode: 你好世界")
        self.assertIn("你好世界", note.content)

    def test_note_with_html_content(self):
        """
        Test note creation with HTML content

        Returns:
            None: Test passes if HTML content is handled correctly
        """
        response = self.client.post(reverse("note_create"), {
            "title": "HTML Test",
            "content": "<script>alert('test')</script><p>Hello</p>"
        })
        self.assertEqual(response.status_code, 302)
        note = Note.objects.get(title="HTML Test")
        self.assertIn("<script>alert('test')</script>", note.content)
