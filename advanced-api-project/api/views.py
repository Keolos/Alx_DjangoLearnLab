from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

# ================================
# BOOK CRUD VIEWS
# ================================

class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves a list of all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves a single book by its ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<id>/update/
    Updates an existing book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Deletes a book.
    Only accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ================================
# OPTIONAL: VIEWSET IMPLEMENTATION
# ================================

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting books.
    Combines all CRUD operations in one class.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
