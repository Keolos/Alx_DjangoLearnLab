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