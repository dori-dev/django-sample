from django import forms
from django.contrib.auth.models import User

INPUT_CLASS = {
    'class': 'form-control'
}


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'email', 'password')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': ''
                }
            ),
            'last_name': forms.TextInput(attrs=INPUT_CLASS),
            'username': forms.TextInput(attrs=INPUT_CLASS),
            'email': forms.EmailInput(attrs=INPUT_CLASS),
            'password': forms.PasswordInput(attrs=INPUT_CLASS)
        }
        help_texts = {
            'username': None
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(
        help_text=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': ''
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=INPUT_CLASS
        )
    )
