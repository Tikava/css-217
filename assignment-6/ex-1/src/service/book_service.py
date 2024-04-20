from src.database import Database
from config.config import DATABASE_NAME
import datetime

class BookService:
    
    def __init__(self):
        self.db = Database(DATABASE_NAME)
    
    def add_book(self, book):
        query = """INSERT INTO books(title, isbn) VALUES (?, ?)"""
        self.db.execute_query(query, (book.title, book.isbn))
        
        book_id = self.db.cursor.lastrowid
        
        for author_name in book.authors:
            author_id = self.db.execute_query("SELECT id FROM authors WHERE name = ?", (author_name,))
            if not author_id:
                self.db.execute_query("INSERT INTO authors(name) VALUES (?)", (author_name,))
                author_id = self.db.cursor.lastrowid
            else:
                author_id = author_id[0][0]
            self.db.execute_query("INSERT INTO book_authors(book_id, author_id) VALUES (?, ?)", (book_id, author_id))
    
    def delete_book(self, isbn):
        book_id_result = self.db.execute_query("SELECT id FROM books WHERE isbn = ?", (isbn,))
        if book_id_result:
            book_id = book_id_result[0][0]
        else:
            return "Book not found"
        
        self.db.execute_query("DELETE FROM book_authors WHERE book_id = ?", (book_id,))        
        self.db.execute_query("DELETE FROM books WHERE id = ?", (book_id,))
        
    def is_book_available(self, book_id):
        result = self.db.execute_query("SELECT COUNT(*) FROM borrow_history WHERE book_id = ? AND return_date IS NULL", (book_id,))
        return result[0][0] == 0
        
    def borrow_book(self, book_id):
        borrow_date = datetime.date.today()
        self.db.execute_query("INSERT INTO borrow_history(book_id, borrow_date) VALUES (?, ?)",
                        (book_id, borrow_date))
    
    def return_book(self, book_id):
        return_date = datetime.date.today()
        self.db.execute_query("UPDATE borrow_history SET return_date = ? WHERE book_id = ?",
                        (return_date, book_id))
    
    # Seaching queries        
    
    def search_book_by_title(self, title):
        return self.db.execute_query(f"""SELECT books.title, authors.name 
                        FROM books 
                        INNER JOIN book_authors ON books.id = book_authors.book_id
                        INNER JOIN authors ON book_authors.author_id = authors.id
                        WHERE books.title LIKE '%{title}%'
                        """)
    
    def search_books_by_author(self, author):
        return self.db.execute_query(f"""
                                SELECT books.title, authors.name
                                FROM books 
                                INNER JOIN book_authors ON books.id = book_authors.book_id
                                INNER JOIN authors ON book_authors.author_id = authors.id
                                WHERE authors.name LIKE '%{author}%'
                                """)