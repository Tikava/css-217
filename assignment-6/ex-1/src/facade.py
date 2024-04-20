from src.service.book_service import BookService
from src.service.author_service import AuthorService

class LibraryFacade:
    def __init__(self):
        self.book_service = BookService()
        self.author_service = AuthorService()
    
    def add_book(self, book):
        self.book_service.add_book(book)
        
    def delete_book(self, isbn):
        self.book_service.delete_book(isbn)
    
    def is_book_available(self, book_id):
        return self.book_service.is_book_available(book_id)
    
    def borrow_book(self, book_id):
        self.book_service.borrow_book(book_id)
    
    def return_book(self, book_id):
        self.book_service.return_book(book_id)
        
    def search_book_by_title(self, title):
        return self.book_service.search_book_by_title(title)
    
    def search_books_by_author(self, author):
        return self.book_service.search_books_by_author(author)
    
    
    #Author management
    
    def add_auhtor(self, author_name):
        self.author_service.add_author(author_name)
        
    def search_authors_by_book_title(self, title):
        return self.author_service.search_authors_by_book_title(title)