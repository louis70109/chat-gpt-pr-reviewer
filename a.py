class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Added book: " + book)  # 錯誤：應該使用 str(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Removed book: " + book)  # 錯誤：應該使用 str(book)
                return
        print("Book not found")

    def list_books(self):
        if len(self.books) == 0:  # 不良習慣：應該使用 if not self.books
            print("No books in the library")
        else:
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Found book: " + book)  # 錯誤：應該使用 str(book)
                return
        print("Book not found")

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

        if choice == 1:  # 錯誤：應該使用 choice == "1"
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year of publication: ")
            book = Book(title, author, year)
            library.add_book(book)
        elif choice == 2:  # 錯誤：應該使用 choice == "2"
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == 3:  # 錯誤：應該使用 choice == "3"
            library.list_books()
        elif choice == 4:  # 錯誤：應該使用 choice == "4"
            title = input("Enter book title to find: ")
            library.find_book(title)
        elif choice == 5:  # 錯誤：應該使用 choice == "5"
            print("Exiting the program...")
            break
        else:
            print("Invalid choice, please try again.")  # 錯誤：這個訊息應該更具體一些

if __name__ == "__main__":
    main()
