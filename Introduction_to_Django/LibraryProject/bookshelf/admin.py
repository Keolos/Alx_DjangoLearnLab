from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show in list view
    list_filter = ('publication_year', 'author')            # Enable filtering
    search_fields = ('title', 'author')                     # Enable search
    ordering = ('publication_year', 'title')                # Default ordering
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'publication_year', 'isbn')
        }),
    )
    readonly_fields = ('isbn',)  # Make ISBN read-only in admin
    prepopulated_fields = {'isbn': ('title',)}  # Automatically fill ISBN based on title    
    def get_queryset(self, request):
        """Customize the queryset to include only books published after 2000."""
        qs = super().get_queryset(request)
        return qs.filter(publication_year__gt=2000)