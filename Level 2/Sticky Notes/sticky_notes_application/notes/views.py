"""
Views for the sticky notes application

This module contains all the view functions that handle HTTP requests
and responses for the sticky notes application. It implements the
complete CRUD (Create, Read, Update, Delete) functionality for notes

The views follow Django's function-based view pattern and include
proper form handling, validation, user feedback, and redirects
"""

# ============= Third-Party Imports =============
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# ========== Local Application Imports ==========
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Display all sticky notes in chronological order

    Retrieves all notes from the database and displays them in a list format,
    sorted by creation date (newest first). This is the main landing page
    of the application where users can view all their notes and access
    navigation to create new notes or edit existing ones

    Arguments:
        request: The HTTP request object

    Returns:
        Rendered template with list of notes and page title
    """
    # Fetch all notes from the database, newest first
    notes = Note.objects.all().order_by('-created_at')

    # Render notes to the main list page
    context = {
        "notes": notes,
        "page_title": "Sticky Notes"
    }
    return render(request, "notes/note_list.html", context)


def note_detail(request, pk):
    """
    Display the full content of a specific sticky note

    Shows the complete details of a single note including its title, content,
    and creation timestamp. Provides navigation options to edit or delete
    the note, or return to the main list

    Arguments:
        request: The HTTP request object
        pk: Primary key of the note to display

    Returns:
        Rendered template with the specific note's details
    """
    # Retrieve the specific note or return 404 if not found
    note = get_object_or_404(Note, pk=pk)

    # Render the note detail page
    return render(request, "notes/note_detail.html", {"note": note})


def note_create(request):
    """
    Handle creation of new sticky notes

    Processes both GET requests (display empty form) and POST requests
    (save new note). Validates form data and creates a new note in the
    database. Redirects to the note list with a success message upon
    successful creation

    Arguments:
        request: The HTTP request object

    Returns:
        Rendered form template or redirect to note list
    """
    if request.method == "POST":
        # Handle form submission
        form = NoteForm(request.POST)
        if form.is_valid():
            # Save new note to the database
            form.save()
            messages.success(request, "Note created successfully!")
            return redirect("note_list")
    else:
        # Display an empty form for new note creation
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_update(request, pk):
    """
    Handle updating existing sticky notes

    Processes both GET requests (display pre-filled form) and POST requests
    (save updated note). Validates form data and updates the existing note
    in the database. Redirects to the note list with a success message
    upon successful update

    Arguments:
        request: The HTTP request object
        pk: Primary key of the note to update

    Returns:
        Rendered form template or redirect to note list
    """
    # Fetch the note to be updated
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        # Handle form submission with updated data
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # Save the updated note to the database
            form.save()
            messages.success(request, "Note updated successfully!")
            return redirect("note_list")
    else:
        # Display form pre-filled with existing note data
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """
    Handle deletion of sticky notes

    Processes both GET requests (display confirmation page) and POST requests
    (perform deletion). Removes the note from the database and redirects
    to the note list with a success message. Uses confirmation page to
    prevent accidental deletions

    Arguments:
        request: The HTTP request object
        pk: Primary key of the note to delete

    Returns:
        Rendered confirmation template or redirect to note list
    """
    # Fetch the note to be deleted
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        # Delete the note after confirmation
        note.delete()
        messages.success(request, "Note deleted successfully!")
        return redirect("note_list")

    # Render the delete confirmation page
    return render(request, "notes/note_confirm_delete.html", {"note": note})
