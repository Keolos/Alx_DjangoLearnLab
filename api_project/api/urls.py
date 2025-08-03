from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListView, add_book, edit_book, delete_book,
    book_detail, book_list, profile_view, change_password, user_profile,
    BookList, BookViewSet
)

# Router for the ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    # Template-based views
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
    path('api/books-list/', BookList.as_view(), name='book-list-api'),
    path('api/', include(router.urls)),  # include all ViewSet routes
]
