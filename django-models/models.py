# Recreate directory for new Django project `django-models` with `relationship_app` and necessary files

# Define paths
from Introduction_to_Django.LibraryProject.bookshelf import models


project_dir = Path("/mnt/data/django-models")
app_dir = project_dir / "relationship_app"

# Create directory structure
app_dir.mkdir(parents=True, exist_ok=True)

# Define models.py content
models_py = from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Define query_samples.py content
query_samples_py = from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


# Write files
(app_dir / "models.py").write_text(models_py, encoding="utf-8")
(app_dir / "query_samples.py").write_text(query_samples_py, encoding="utf-8")

# Return path for user to download
project_dir.as_posix()
