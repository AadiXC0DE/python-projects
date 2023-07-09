#Library management system 
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            print("Library Books:")
            for book in self.books:
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"ISBN: {book.isbn}")
                print("--------------")

    def checkout_book(self, book):
        if book.is_available:
            book.is_available = False
            print(f"Successfully checked out '{book.title}'.")
        else:
            print(f"'{book.title}' is not available for checkout.")

    def return_book(self, book):
        if not book.is_available:
            book.is_available = True
            print(f"Successfully returned '{book.title}'.")
        else:
            print(f"'{book.title}' is already available.")


def main():
    library = Library()

    # Create and add books to the library
    book1 = Book("Book1", "Author1", "ISBN1")
    book2 = Book("Book2", "Author2", "ISBN2")
    book3 = Book("Book3", "Author3", "ISBN3")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Display all books")
        print("2. Search a book")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the title of the book: ")
            book = library.search_book(title)
            if book:
                print(f"Book found: '{book.title}' by {book.author}")
            else:
                print("Book not found.")
        elif choice == "3":
            title = input("Enter the title of the book to checkout: ")
            book = library.search_book(title)
            if book:
                library.checkout_book(book)
            else:
                print("Book not found.")
        elif choice == "4":
            title = input("Enter the title of the book to return: ")
            book = library.search_book(title)
            if book:
                library.return_book(book)
            else:
                print("Book not found.")
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
