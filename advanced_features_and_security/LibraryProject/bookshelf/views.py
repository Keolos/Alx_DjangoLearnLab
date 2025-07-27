from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

# --- Book List View ---
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# --- Create Book View ---
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Only users with can_create permission can access
    return render(request, 'bookshelf/create_book.html')
