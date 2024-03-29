from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def check_out(self):
        pass
    
    @abstractmethod
    def return_item(self):
        pass
    
class Book(LibraryItem):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def check_out(self):
        print(f"Book '{self.title}' by {self.author} has been checked out.")

    def return_item(self):
        print(f"Book '{self.title}' by {self.author} has been returned.")

class Magazine(LibraryItem):
    def __init__(self, title, issue, publisher):
        self.title = title
        self.issue = issue
        self.publisher = publisher
        
    def check_out(self):
        print(f"Magazine '{self.title}' by {self.publisher} has been checked out.")
    
    def return_item(self):
        print(f"Magazine '{self.title}' by {self.publisher} has been returned.")
    
class CD(LibraryItem):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        
    def check_out(self):
        print(f"CD '{self.title}' by {self.artist} has been checked out.")
    
    def return_item(self):
        print(f"CD '{self.title}' by {self.artist} has been returned.")

class User(ABC):
    @abstractmethod
    def browse_catalog(self):
        pass
    
    @abstractmethod
    def check_out_item(self):
        pass
    
    @abstractmethod
    def return_item(self):
        pass
    
class Librarian(User):
    def browse_catalog(self):
        print("Librarian browsing catalog")
    
    def check_out_item(self, item):
        item.check_out()
        
    def return_item(self, item):
        item.return_item()