from django.db import models
from rest_framework import serializers
from .models import book, author

urlpatterns = [
    # Define your API URLs here
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),    
]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['id', 'title', 'author', 'published_date', 'isbn']
        read_only_fields = ['id']
        extra_kwargs = {
            'title': {'required': True},
            'author': {'required': True},
            'published_date': {'required': True},
            'isbn': {'required': True, 'max_length': 13}
        }

    def create(self, validated_data):
        return book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = ['id', 'name', 'email']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True, 'max_length': 100}
        }

    def create(self, validated_data):
        return author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
from django.urls import path, include
from django.contrib import admin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.urls import reverse_lazy
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import book
from .forms import BookForm
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
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})
from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import BookListView, add_book, edit_book, delete_book
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListView, add_book, edit_book, delete_book, book_detail, book_list, profile_view, change_password, user_profile, BookViewSet, BookListAPI

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
    path('detail/<int:pk>/', book_detail, name='book_detail'),
    path('all/', book_list, name='all_books'),

    path('profile/', profile_view, name='profile'),
    path('profile/change-password/', change_password, name='change_password'),
    path('user-profile/', user_profile, name='user_profile'),

    # API endpoints
    path('api/books-list/', BookListAPI.as_view(), name='book-list-api'),
    path('api/', include(router.urls)),
]
