from django import forms
from .models import Note


class NoteCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')
        labels = {
            'body': 'Detail'
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': ''
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }
