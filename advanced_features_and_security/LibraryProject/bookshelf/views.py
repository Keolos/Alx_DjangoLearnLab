from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Only users with can_create permission can access
    return render(request, 'bookshelf/create_book.html')
