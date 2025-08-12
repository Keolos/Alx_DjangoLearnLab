from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    update_book,
    delete_book,
    BookViewSet
)

# DRF router for viewsets
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # Class-based view URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Function-based API endpoints for update and delete
    path('books/update/<int:pk>/', update_book, name='api-book-update'),
    path('books/delete/<int:pk>/', delete_book, name='api-book-delete'),

    # DRF router URLs
    path('', include(router.urls)),
]
