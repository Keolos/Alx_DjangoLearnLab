from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
orwell = Author.objects.get(name='George Orwell')
books_by_orwell = Book.objects.filter(author=orwell)
print("Books by George Orwell:", books_by_orwell)

# 2. List all books in a specific library
central_library = Library.objects.get(name='Central Library')
library_books = central_library.books.all()
print("Books in Central Library:", library_books)

# 3. Retrieve the librarian for a specific library
librarian = Librarian.objects.get(library=central_library)
print("Librarian for Central Library:", librarian.name)
