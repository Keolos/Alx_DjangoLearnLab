from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Secure form for creating and editing Book objects.
    Django handles input validation and CSRF automatically.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# LibraryProject/bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Form for creating and validating Book entries."""
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']