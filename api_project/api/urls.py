from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListView, add_book, edit_book, delete_book, 
    book_detail, book_list, profile_view, change_password, user_profile, 
    BookViewSet, BookListAPI
)

router = DefaultRouter()
router.register(r'books', BookViewSet)

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
    path('api/books-list/', BookListAPI.as_view(), name='book-list-api'),
    path('api/', include(router.urls)),
]
from .views import BookListAPI as BookList  # alias

path('api/books-list/', BookList.as_view(), name='book-list-api'),


from .views import BookList

path('api/books-list/', BookList.as_view(), name='book-list-api'),
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
class BookListAPI(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
from rest_framework import viewsets
from .models import book
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        return Response(serializer.data)
from rest_framework.decorators import action
from rest_framework.response import Response        
from rest_framework import viewsets
from .models import book
from .serializers import BookSerializer
from rest_framework.routers import DefaultRouter
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        router = DefaultRouter()
        router.register(r'books_all', BookViewSet, basename='book_all')

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
        return Response(serializer.data)
        instance.delete()
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import book
from .serializers import BookSerializer
class BookListAPI(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
        # Remove this line. `instance.delete()` is not needed in perform_update and will cause errors.

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]