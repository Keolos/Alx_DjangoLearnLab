from django.db import models
from datetime import date

class Author(models.Model):
    """
    Author model represents a writer.
    Fields:
        name (str): The full name of the author.
    Relationship:
        One Author can have many Books (One-to-Many).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model stores details of books written by authors.
    Fields:
        title (str): The title of the book.
        publication_year (int): Year the book was published.
        author (FK): Link to the Author model.
    Relationship:
        Many Books can be linked to one Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(default=date.today)
    isbn = models.CharField(max_length=13, null=True, blank=True)


    def __str__(self):
        return self.title
