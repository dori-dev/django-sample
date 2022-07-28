from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from .forms import UserRegistrationForm, UserLoginForm


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


def login_view(request: WSGIRequest):
    next_page = request.GET.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            user = authenticate(
                request,
                username=user_data['username'],
                password=user_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    'you <strong>logged in</strong> successfully.',
                    extra_tags='success'
                )
                if next_page is None:
                    return redirect('notes:index')
                else:
                    return redirect(next_page)
            else:
                messages.error(
                    request,
                    '<strong>username</strong> or '
                    '<strong>password</strong> is wrong!',
                    extra_tags='danger'
                )
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
