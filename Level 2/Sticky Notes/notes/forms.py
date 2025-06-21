"""
Forms for the sticky notes application

This module defines the forms used for user input in the sticky notes
application. It contains the NoteForm which provides an interface for creating
and editing notes with proper validation

The forms extend Django's ModelForm to automatically generate form
fields based on the Note model and handle data validation. This ensures
consistency between the database schema and form structure while providing
built-in validation and error handling

Features:
- Automatic field generation from Note model
- Built-in validation for required fields
- User-friendly error messages
- Support for both create and update operations
- Clean separation of concerns between data and presentation
"""

# ============= Third-Party Imports =============
from django import forms

# ========== Local Application Imports ==========
from .models import Note


class NoteForm(forms.ModelForm):
    """
    Form for creating and editing sticky notes

    This form provides an interface for inputting note data
    It automatically handles validation and rendering of the title and content
    fields based on the Note model. The form supports both creating new notes
    and updating existing ones through Django's ModelForm functionality

    The form inherits from Django's ModelForm, which automatically:
    - Generates form fields based on the model's field definitions
    - Handles data validation against model constraints
    - Provides error messages for invalid input
    - Manages the relationship between form data and model instances
    """

    class Meta:
        """
        Meta class defining form configuration

        This Meta class specifies how the form should behave and which
        model fields should be included. It ensures the form only exposes
        the necessary fields and maintains consistency with the model

        Attributes:
            model (class): The Django model class to base the form on
            fields (list): List of field names to include in the form

        Fields:
            title (CharField): Text input for the note title with max length
                               validation
            content (TextField): Multi-line textarea for the note content
        """
        # Reference to the Note model for automatic field generation
        model = Note
        # Only include 'title' and 'content' fields in the form
        # The id and created_at fields are handled automatically
        fields = ["title", "content"]
