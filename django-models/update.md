# Update the Book Title

\`\`\`python
book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=book.id)
print(updated_book)
\`\`\`

**Output:**
\`\`\`
Nineteen Eighty-Four by George Orwell (1949)
\`\`\`
