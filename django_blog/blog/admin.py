from django.contrib import admin
from .models import Post
from django.urls import reverse


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
    ordering = ('published_date',)