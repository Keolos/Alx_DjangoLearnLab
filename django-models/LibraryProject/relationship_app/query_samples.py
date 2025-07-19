from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., "George Orwell")
george = Author.objects.get(name="George Orwell")
books_by_george = Book.objects.filter(author=george)
print("Books by George Orwell:")
for book in books_by_george:
    print("-", book.title)

# 2. List all books in a specific library (e.g., "Central Library")
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print("-", book.title)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian of {library.name}: {librarian.name}")
