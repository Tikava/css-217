from src.database import Database
from config.config import DATABASE_NAME

class AuthorService:
    def __init__(self):
        self.db = Database(DATABASE_NAME)
        
    def add_author(self, author_name):
        self.db.execute_query("INSERT INTO authors(name) VALUES (?)", (author_name,))

    def search_authors_by_book_title(self, title):
        query = """
            SELECT authors.name 
            FROM authors
            INNER JOIN book_authors ON authors.id = book_authors.author_id
            INNER JOIN books ON book_authors.book_id = books.id
            WHERE books.title LIKE ?
        """
        return self.db.execute_query(query, ('%' + title + '%',))
