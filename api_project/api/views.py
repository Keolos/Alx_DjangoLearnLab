from django.shortcuts import render

# Create your views here.
class BookListView(ListView):
    model = book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10
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
@permission_required('api.delete_book')
def delete_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})
@permission_required('api.view_book')
def book_detail(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    return render(request, 'book_detail.html', {'book': book_instance})
@permission_required('api.view_book')
def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from .models import book
from .forms import BookForm
from django.views.generic import ListView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
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
from rest_framework import serializers
from .models import book
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
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect   
@login_required
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
@login_required
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user}) 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
@login_required
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from .models import book
from .forms import BookForm
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
    return render(request, 'edit_book.html', {'book': book_instance})
@permission_required('api.delete_book')
def delete_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})
@permission_required('api.view_book')
def book_detail(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    return render(request, 'book_detail.html', {'book': book_instance})
@permission_required('api.view_book')
def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
@permission_required('api.view_book')
def book_detail(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    return render(request, 'book_detail.html', {'book': book_instance})
def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})  
@permission_required('api.view_book')
def book_detail(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    return render(request, 'book_detail.html', {'book': book_instance})
@permission_required('api.view_book')
def book_list(request):
    books = book.objects.all()
    return render(request, 'book_list.html', {'books': books})
def delete_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})
def delete_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance}) 
def delete_book(request, pk):
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})