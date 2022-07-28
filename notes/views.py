from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.handlers.wsgi import WSGIRequest
from .models import Note


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
