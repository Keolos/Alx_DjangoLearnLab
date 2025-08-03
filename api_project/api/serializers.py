from django.db import models
from rest_framework import serializers
from .models import book, author

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
            return redirect('book_list')
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
        return instance
        return redirect('author_list')  
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required  
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
    return render(request, 'add_book.html', {'form': form})
    return render(request, 'add_book.html', {'form': form})
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
@login_required
@permission_required('api.add_author')
def add_author(request):
    if login_required(request):
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('author_list')
        else:
            form = AuthorForm()
        return render(request, 'add_author.html', {'form': form})
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
@login_required
@permission_required('api.change_book')
def change_book(request, book_id):
    book_instance = get_object_or_404(book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book_instance)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book_instance.id)
    else:
        form = BookForm(instance=book_instance)
    return render(request, 'change_book.html', {'form': form})

from django.shortcuts import get_object_or_404  
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect

@permission_required('api.delete_book')
def delete_book(request, pk):   
    book_instance = get_object_or_404(book, pk=pk)
    if request.method == 'POST':
        book_instance.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book_instance})