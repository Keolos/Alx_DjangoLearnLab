from relationship_app.models import Author, Book, Library, Librarian

# Variable for dynamic lookup
library_name = "Central Library"

# 1. Query all books by a specific author
orwell = Author.objects.get(name='George Orwell')
books_by_orwell = Book.objects.filter(author=orwell)
print("Books by George Orwell:", books_by_orwell)

# 2. List all books in a specific library
library = Library.objects.get(name=library_name)  # ✅ Required line
library_books = library.books.all()
print(f"Books in {library_name}:", library_books)

# 3. Retrieve the librarian for the specific library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}:", librarian.name)
