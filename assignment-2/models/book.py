from absraction.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def check_out(self):
        print(f"Book '{self.title}' by {self.author} has been checked out.")

    def return_item(self):
        print(f"Book '{self.title}' by {self.author} has been returned.")