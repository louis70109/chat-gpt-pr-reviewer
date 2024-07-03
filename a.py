import datetime
import logging

logging.basicConfig(level=logging.INFO)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.added_date = datetime.datetime.now()  # 問題1: 未使用的屬性

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if isinstance(book, Book):
            self.books[book.title] = book  # 問題2: 書名作為鍵可能導致重複
            logging.info(f"Added book: {book}")
        else:
            logging.error("Invalid book object")

    def remove_book(self, title):
        if title in self.books:
            removed_book = self.books.pop(title)
            logging.info(f"Removed book: {removed_book}")
        else:
            logging.warning("Book not found")  # 問題3: 應該使用 logging.info 而不是 logging.warning

    def list_books(self):
        if not self.books:
            logging.info("No books in the library")
        else:
            for title, book in self.books.items():
                logging.info(book)

    def find_book(self, title):
        book = self.books.get(title)
        if book:
            logging.info(f"Found book: {book}")
        else:
            logging.warning("Book not found")  # 問題4: 應該使用 logging.info 而不是 logging.warning

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. List books")
        print("4. Find book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year of publication: ")
            try:
                year = int(year)  # 問題5: 應該有更多的輸入驗證
            except ValueError:
                logging.error("Year must be a number")
                continue
            book = Book(title, author, year)
            library.add_book(book)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            title = input("Enter book title to find: ")
            library.find_book(title)
        elif choice == "5":
            logging.info("Exiting the program...")
            break
        else:
            logging.error("Invalid choice, please try again.")  # 問題6: 應該使用 logging.warning 而不是 logging.error

if __name__ == "__main__":
    main()
