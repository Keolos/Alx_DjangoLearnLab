from relationship_app.models import Author, Book, Library, Librarian

# Define variable inputs
author_name = "George Orwell"
library_name = "Central Library"

# 1. Query all books by a specific author
author = Author.objects.get(name=author_name)  # ✅ Required line 1
books_by_author = Book.objects.filter(author=author)  # ✅ Required line 2
print(f"Books by {author_name}:", books_by_author)

# 2. List all books in a specific library
library = Library.objects.get(name=library_name)  # ✅ Already required earlier
library_books = library.books.all()
print(f"Books in {library_name}:", library_books)

# 3. Retrieve the librarian for the specific library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}:", librarian.name)
