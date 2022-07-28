from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from .forms import UserRegistrationForm


def register_view(request: WSGIRequest):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user: User = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            messages.success(
                request,
                'you <strong>registered</strong> successfully.',
                extra_tags='success'
            )
            if next_page is None:
                return redirect('notes:index')
            else:
                return redirect(next_page)
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)
