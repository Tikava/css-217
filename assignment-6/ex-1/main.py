from src.database import Database
from src.facade import LibraryFacade
from src.models import Book
from config.config import DATABASE_NAME

db = Database(DATABASE_NAME)
db.connect()

def init():
    db.execute_query('''CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT
            )''')
        
    db.execute_query('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        isbn TEXT
        )''')
    
    db.execute_query('''CREATE TABLE IF NOT EXISTS book_authors (
        book_id INTEGER,
        author_id INTEGER,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (author_id) REFERENCES authors(id),
        PRIMARY KEY (book_id, author_id)
        )''')
    
    db.execute_query('''CREATE TABLE IF NOT EXISTS borrow_history (
        id INTEGER PRIMARY_KEY,
        book_id INTEGER,
        borrow_date DATE,
        return_date DATE,
        FOREIGN KEY (book_id) REFERENCES books(id)
        )
        ''')
        

def main():
    init()
    
    facade = LibraryFacade()
    
    print("Welcome to Library system:\nYou can:\n1.Add book\n2.Remove book\n3.Borrow book\n4.Return book\n5.Search\n6.Check availability of book\n7.Add author")
    choice = int(input("Please enter your choice(e.g number): "))
    
    if choice == 1:
        title = input("Enter the title of the book: ")
        author_input = input("Enter the author(s) of the book (separated by commas): ")
        authors = [author.strip() for author in author_input.split(',')]
        isbn = input("Enter the ISBN of the book: ")
        book = Book(title, authors, isbn)
        facade.add_book(book)
        print("Book added successfully.")

        
    elif choice == 2:
        isbn = input("Enter the ISBN of the book you want to remove: ")
        facade.delete_book(isbn)
        print("Book removed successfully.")
        
    elif choice == 3:
        book_id = input("Enter the ID of the book you want to borrow: ")
        if facade.is_book_available(book_id):
            facade.borrow_book(book_id)
            print("Book borrowed successfully.")
        else:
            print("Book is not available for borrowing.")
        
    elif choice == 4:
        book_id = input("Enter the ID of the book you want to return: ")
        facade.return_book(book_id)
        print("Book returned successfully.")
        
    elif choice == 5:
        search_query = input("Enter the title or author to search: ")
        results = facade.search_book_by_title(search_query) + facade.search_books_by_author(search_query)
        if results:
            print("Search results:")
            for result in results:
                print(result)
        else:
            print("No matching books found.")
            
    elif choice == 6:
        book_id = input("Enter the ID of the book you want to check availability for: ")
        if facade.is_book_available(book_id):
            print("Book is available.")
        else:
            print("Book is not available.")
            
    elif choice == 7:
        author_name = input("Enter the name of the author to add: ")
        facade.add_author(author_name)
        print("Author added successfully.")
        
    else:
        print("Invalid choice. Please enter a valid option.")


if __name__ == '__main__':
    main()