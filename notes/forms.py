from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Текст заметки', 'rows': 3}
            ),
        }
