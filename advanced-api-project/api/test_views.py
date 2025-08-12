from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from api.models import Book

User = get_user_model()

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a regular user and an authenticated client
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.admin_user = User.objects.create_superuser(
            username="admin", password="adminpass123"
        )

        # Authenticate as regular user by default
        self.client.login(username="testuser", password="password123")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Book One", author="Author A", publication_year=2020, genre="Fiction"
        )
        self.book2 = Book.objects.create(
            title="Book Two", author="Author B", publication_year=2021, genre="Science"
        )

        self.list_url = reverse("book-list")  # from DRF router or URL name
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "New Book",
            "author": "Author C",
            "publication_year": 2022,
            "genre": "Drama"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest("id").title, "New Book")

    def test_list_books(self):
        """Test listing books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book(self):
        """Test updating a book"""
        data = {"title": "Updated Title"}
        response = self.client.patch(self.detail_url(self.book1.id), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book_requires_admin(self):
        """Ensure only admin can delete"""
        # Try deleting as regular user
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Login as admin
        self.client.logout()
        self.client.login(username="admin", password="adminpass123")
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_genre(self):
        """Test filtering by genre"""
        response = self.client.get(f"{self.list_url}?genre=Fiction")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["genre"] == "Fiction" for book in response.data))

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.list_url}?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Book One" in book["title"] for book in response.data))

    def test_order_books_by_year(self):
        """Test ordering books by publication_year"""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
