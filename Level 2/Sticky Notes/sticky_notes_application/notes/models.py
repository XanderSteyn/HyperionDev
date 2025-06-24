"""
Models for the sticky notes application

This module defines the data models that represent the core entities
of the sticky notes application. It contains the Note model which
stores all the data for individual sticky notes including title,
content, and creation timestamp

The models use Django's ORM to provide database abstraction and include
methods for data validation and representation
"""

# ============= Third-Party Imports =============
from django.db import models


class Note(models.Model):
    """
    Represents a sticky note in the application

    This model stores the core data for each sticky note including its title,
    content, and creation timestamp. The model is designed to be simple,
    providing the essential functionality for a sticky notes application

    Fields:
        title: The note's title/heading (max 255 characters for UI consistency)
        content: The main text content of the note (unlimited length)
        created_at: Automatically set timestamp when note is created

    Methods:
        __str__: Returns the note title for admin interface and debugging
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    # Automatically adds current timestamp when the note is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the note

        Returns:
            str: The title of the note, used for display in the admin
                 interface and debugging
        """
        return self.title
