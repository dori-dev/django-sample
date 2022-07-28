from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.handlers.wsgi import WSGIRequest
from .models import Note
from .forms import NoteCreateFrom


def index(request: WSGIRequest):
    if request.user.is_anonymous:
        notes = None
    else:
        notes = Note.objects.filter(
            author=request.user
        ).order_by('-created')
    context = {
        "notes": notes
    }
    return render(request, "notes/index.html", context)


def detail(request: WSGIRequest, pk: int):
    note = get_object_or_404(Note, pk=pk)
    if note.author != request.user:
        raise Http404
    context = {
        "note": note
    }
    return render(request, "notes/detail.html", context)


def create(request: WSGIRequest):
    if request.method == "POST":
        form = NoteCreateFrom(request.POST)
        if form.is_valid():
            note: Note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes:index')
    else:
        form = NoteCreateFrom()
    context = {
        'form': form,
    }
    return render(request, "notes/create.html", context)
