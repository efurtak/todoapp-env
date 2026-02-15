from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
        # Opcjonalnie dodaj style Tailwind do widgetów
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name-input'}),
        }