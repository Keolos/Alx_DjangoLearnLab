from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # Show these in list view
    search_fields = ('title', 'author')                      # Allow admin to search by title or author
    list_filter = ('publication_year',)                      # Filter by publication year
