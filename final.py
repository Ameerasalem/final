class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level
        self.is_available = True


class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    # TODO : implement member method
    def borrow_book(self, book):
        if book.is_available :
            book.is_available = False
            print("borrowed successfully.")
        else:
            print("Book cannot be borrowed.")
    # def return_book(self, book):


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # TODO : implement Library methods
    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        for book in self.books:
            print(
                f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}"
                f", Level: {book.level}, Availability: "
                f"{'Available' if book.is_available else 'Not Available'}")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def display_members(self):
        for member in self.members:
            print(
                f"ID: {member.member_id}, Name: {member.name}, Email: {member.email}"
                f", Level: {member.level}, Borrowed Books: "
                f"{', '.join([book.title for book in member.borrowed_books])}")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


library = Library()
print(' Welcome to the Library System '.center(100,'-'))
while True:
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. Show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("Enter your choice: ")

# TODO : implement the menu