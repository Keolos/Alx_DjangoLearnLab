from django.urls import path
from .views import list_books, LibraryDetailView



urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
]

from .views import login_view, logout_view, register_view

urlpatterns += [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


from .views import admin_view, librarian_view, member_view


urlpatterns += [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
]


from .views import add_book, edit_book, delete_book

urlpatterns += [
    path('books/add/', add_book, name='add_book'),
    path('books/edit/', edit_book, name='edit_book'),
    path('books/delete/', delete_book, name='delete_book'),
]
