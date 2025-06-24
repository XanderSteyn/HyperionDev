"""
Initial migration for the sticky notes application

This migration creates the foundational database structure for the sticky notes
application. It establishes the Note model table with all necessary fields
for storing note data including title, content, and creation timestamp

Migration Details:
- Creates the 'notes_note' table in the database
- Defines the Note model with auto-incrementing primary key
- Sets up title field with maximum length constraint
- Configures content field for storing note text
- Adds automatic timestamp for creation tracking

Dependencies: None (initial migration)
Operations: Single CreateModel operation for Note
"""

# ============= Third-Party Imports =============
from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Initial migration class for the sticky notes application

    This migration establishes the core database schema for the notes app
    It creates the Note model table with all required fields and constraints

    Attributes:
        initial (bool): Indicates this is the first migration for the app
        dependencies (list): Empty list since this is the initial migration
        operations (list): List of database operations to perform
    """

    # Flag indicating this is the first migration for the notes app
    initial = True

    # No dependencies since this is the initial migration
    dependencies = []

    # List of database operations to execute
    operations = [
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                # Title field: stores the note's title with max length of
                # 255 characters
                ("title", models.CharField(max_length=255)),
                # Content field: stores the main text content of the note
                ("content", models.TextField()),
                # Created_at field: automatically set to current timestamp
                # when note is created
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
