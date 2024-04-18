import sqlite3
import datetime

class Database(object):
    
    def __new__(cls, name):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Database, cls).__new__(cls)
            cls.instance.connection = sqlite3.connect(f'{name}.db')
        return cls.instance
    
    def connect(self):
        self.cursor = self.connection.cursor()
        
    def disconnect(self):
        self.cursor.close()
        
    def execute_query(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    
class LibraryFacade(Database):
    
    def __init__(self):
        self.execute_query('''CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT
            )''')
        
        self.execute_query('''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            isbn TEXT
            )''')
        
        self.execute_query('''CREATE TABLE IF NOT EXISTS book_authors (
            book_id INTEGER,
            author_id INTEGER,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (author_id) REFERENCES authors(id),
            PRIMARY KEY (book_id, author_id)
            )''')
        
        self.execute_query('''CREATE TABLE IF NOT EXISTS borrow_history (
            id INTEGER PRIMARY_KEY,
            book_id INTEGER,
            borrow_date DATE,
            return_date DATE,
            FOREIGN KEY (book_id) REFERENCES books(id),
            )
            ''')
        
    def is_book_available(self, book_id):
        result = self.execute_query("SELECT COUNT(*) FROM borrow_history WHERE book_id = ? AND return_date IS NULL", (book_id,))
        return result[0][0] == 0
    
    def add_book(self, book):
        query = """INSERT INTO books(title, isbn) VALUES (?, ?)"""
        self.execute_query(query, (book.title, book.isbn))
        
        book_id = self.cursor.lastrowid
        
        for author_name in book.authors:
            author_id = self.execute_query("SELECT id FROM authors WHERE name = ?", (author_name,))
            if not author_id:
                self.execute_query("INSERT INTO authors(name) VALUES (?)", (author_name,))
                author_id = self.cursor.lastrowid
            else:
                author_id = author_id[0][0]
            
            self.execute_query("INSERT INTO book_authors(book_id, author_id) VALUES (?, ?)", (book_id, author_id))
    
    def delete_book(self, isbn):
        book_id_result = self.execute_query("SELECT id FROM books WHERE isbn = ?", (isbn,))
        if book_id_result:
            book_id = book_id_result[0][0]
        else:
            return "Book not found"
        
        self.execute_query("DELETE FROM book_authors WHERE book_id = ?", (book_id,))        
        self.execute_query("DELETE FROM books WHERE id = ?", (book_id,))
        
    def borrow_book(self, book_id):
        borrow_date = datetime.date.today()
        self.execute_query("INSERT INTO borrow_history(book_id, borrow_date) VALUES (?, ?)",
                        (book_id, borrow_date))
    
    def return_book(self, book_id):
        return_date = datetime.date.today()
        self.execute_query("UPDATE borrow_history SET return_date = ? WHERE book_id = ?",
                        (return_date, book_id))

    def add_author(self, author_name):
        self.execute_query("""INSERT INTO authors(name) VALUES (?)""", (author_name,))

    # Seaching queries
    def search_book_by_title(self, title):
        return self.execute_query(f"""SELECT books.title, authors.name 
                        FROM books 
                        INNER JOIN book_authors ON books.id = book_authors.book_id
                        INNER JOIN authors ON book_authors.author_id = authors.id
                        WHERE books.title LIKE '%{title}%'
                        """)
    
    def search_books_by_author(self, author):
        return self.execute_query(f"""
                                SELECT books.title, authors.name
                                FROM books 
                                INNER JOIN book_authors ON books.id = book_authors.book_id
                                INNER JOIN authors ON book_authors.author_id = authors.id
                                WHERE authors.name LIKE '%{author}%'
                                """)

    def search_authors_by_book_title(self, title):
        return self.execute_query(f"""
                                SELECT authors.name 
                                FROM authors
                                INNER JOIN book_authors ON authors.id = book_authors.author_id
                                INNER JOIN books ON book_authors.book_id = books.id
                                WHERE books.title LIKE '%{title}%'
                                """)

    