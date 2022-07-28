from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from .models import Note
from .forms import NoteCreateUpdateForm


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


@login_required(login_url='accounts:login')
def detail(request: WSGIRequest, pk: int):
    note = get_object_or_404(Note, pk=pk)
    if note.author != request.user:
        raise Http404
    context = {
        "note": note
    }
    return render(request, "notes/detail.html", context)


@login_required(login_url='accounts:login')
def create(request: WSGIRequest):
    if request.method == "POST":
        form = NoteCreateUpdateForm(request.POST)
        if form.is_valid():
            note: Note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(
                request,
                f'"{note.title}" note, '
                '<strong>created</strong> successfully.',
                extra_tags='success'
            )
            return redirect('notes:index')
    else:
        form = NoteCreateUpdateForm()
    context = {
        'form': form
    }
    return render(request, "notes/create.html", context)


@login_required(login_url='accounts:login')
def update(request: WSGIRequest, pk: int):
    note = get_object_or_404(Note, pk=pk)
    if note.author != request.user:
        raise Http404
    if request.method == "POST":
        form = NoteCreateUpdateForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'this to <strong>updated</strong> successfully.',
                extra_tags='success'
            )
            return redirect('notes:detail', pk)
    else:
        form = NoteCreateUpdateForm(instance=note)
    context = {
        'form': form,
        'note': note
    }
    return render(request, "notes/update.html", context)


@login_required(login_url='accounts:login')
def delete(request: WSGIRequest, pk: int):
    note = get_object_or_404(Note, pk=pk)
    if note.author != request.user:
        raise Http404
    note.delete()
    messages.success(
        request,
        f'"{note.title}" note '
        '<strong>deleted</strong> successfully.',
        extra_tags='success'
    )
    return redirect('notes:index')
