class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"{self.title} by {self.author} (E-Book, {self.file_size}MB)"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} (Print Book, {self.page_count} pages)"


class Library:
    def __init__(self):
        self.books = []  # composition: library *contains* books

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return

        print("Books in the Library:")
        for book in self.books:
            print(f"- {book}")
