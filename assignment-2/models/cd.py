from absraction.library_item import LibraryItem

class CD(LibraryItem):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        
    def check_out(self):
        print(f"CD '{self.title}' by {self.artist} has been checked out.")
    
    def return_item(self):
        print(f"CD '{self.title}' by {self.artist} has been returned.")