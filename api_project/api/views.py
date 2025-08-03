from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import book
from .forms import BookForm

# DRF imports
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import BookSerializer


# ============================
#   Template-based views
# ============================

class BookListView(ListView):
    model = book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10


@login_required
@permission_required('api.add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


@login_required
@permission_required('api.change_book')
def edit_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book_instance)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book_instance)
    return render(request, 'edit_book.html', {'form': form, 'book': book_instance})


@login_required
@permission_required('api.delete_book')
def delete_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})


@login_required
@permission_required('api.view_book')
def book_detail(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    return render(request, 'book_detail.html', {'book': book_instance})


@login_required
@permission_required('api.view_book')
def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})


# ============================
#   API views (Django REST Framework)
# ============================

# ListAPIView (Read-only list endpoint)
class BookListAPI(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Full CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        book_instance = self.get_object()
        serializer = self.get_serializer(book_instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def list_books(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_destroy(self, instance):
        instance.delete()
