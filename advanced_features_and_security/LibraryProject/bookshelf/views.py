from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.db.models import Q
from django import forms
from .models import Book


# --- Search Form for Validation ---
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)


# --- Book List View (with search + permission) ---
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


# --- Create Book View ---
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Only users with can_create permission can access
    return render(request, 'bookshelf/create_book.html')
