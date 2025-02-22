class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added {book.title}"

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f"Removed {title}"
        return "Book not found!"

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return f"Found: {book}"
        return "Book not found!"

    def list_books(self):
        return [str(book) for book in self.books] if self.books else "No books available"

    def __str__(self):
        str = ''
        for k in self.books:
            # str = k+","+str
            str = f"{k} , {str}"
        return str
        # return f"{self.title} by {self.author}"


library = Library()
b1 = Book("True Lune: Rejected by my Mate", "Tessa Lilly")
b2 = Book("True Lune: Chaisng the White Wold", "Tessa Lilly")
b3 = Book("True Lune: The Darkness Within", "Tessa Lilly")

print(library.add_book(b1))  
print(library.add_book(b2))  
print(library.add_book(b3))  
# print(library.list_books())  
print(library)
print(library.search_book("True Lune: Rejected by my Mate")) 
print(library.remove_book("True Lune: The Darkness Within")) 
print(library.search_book("True Lune: Rejected")) 
