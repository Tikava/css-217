from abstraction.user import User
        
class Librarian(User):
    def browse_catalog(self):
        print("Librarian is browsing catalog")
    
    def check_out_item(self, item):
        item.check_out()
        
    def return_item(self, item):
        item.return_item()