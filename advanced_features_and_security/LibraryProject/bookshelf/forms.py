from django import forms
from .models import Book

# --- Example Form for CSRF and Validation Demo ---
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# --- Search Form for Validation ---
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

# --- Book Form (ModelForm) ---
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
