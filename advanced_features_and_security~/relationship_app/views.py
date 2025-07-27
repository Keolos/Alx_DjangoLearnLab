from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book, Author
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'




def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def register(request):  # ← rename this
    ...


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import UserProfile


@login_required
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



@permission_required('relationship_app.can_add_book')
def add_book(request):
    return HttpResponse("You have permission to add a book.")

@permission_required('relationship_app.can_change_book')
def edit_book(request):
    return HttpResponse("You have permission to edit a book.")

@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return HttpResponse("You have permission to delete a book.")
