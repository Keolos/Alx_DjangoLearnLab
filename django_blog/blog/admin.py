from django.contrib import admin
from .models import Post, Profile
from django.urls import reverse


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
    ordering = ('published_date',)
    

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_image')
    list_filter = ('user',)
    search_fields = ('user__username',
                     'user__email', 'bio')
    ordering = ('user__username',)


