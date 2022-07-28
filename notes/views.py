from django.shortcuts import render
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
