from django.forms import ModelForm, widgets
from guestbook_app.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'email', 'text']
        widgets = {
            'name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'email': widgets.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'text': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Текст записи',
            }),
        }