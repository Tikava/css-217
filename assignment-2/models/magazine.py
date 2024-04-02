from absraction.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, issue, publisher):
        self.title = title
        self.issue = issue
        self.publisher = publisher
        
    def check_out(self):
        print(f"Magazine '{self.title}' by {self.publisher} has been checked out.")
    
    def return_item(self):
        print(f"Magazine '{self.title}' by {self.publisher} has been returned.")