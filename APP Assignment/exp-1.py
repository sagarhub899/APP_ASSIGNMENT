
# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, "
              f"Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
            return

        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print("Patron ID already exists.")
            return

        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book_id)
            print(f"{patron.name} borrowed '{book.title}'.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book_id in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book_id)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the patron.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books")
        print("-" * 50)

        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            book.display()

    # Display all patrons
    def display_patrons(self):
        print("\nRegistered Patrons")
        print("-" * 50)

        if not self.patrons:
            print("No patrons registered.")
            return

        for patron in self.patrons.values():
            patron.display()
            print()


library = Library()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(Book(book_id, title, author))

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        library.register_patron(Patron(patron_id, name))

    elif choice == "3":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.borrow_book(patron_id, book_id)

    elif choice == "4":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")
        library.return_book(patron_id, book_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
