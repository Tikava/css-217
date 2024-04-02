from models.librarian import Librarian
from models.patron import Patron
from models.book import Book
from models.magazine import Magazine
from models.cd import CD

def main():
    user = None
    while not user:
        user_type = input("Enter the user type (librarian/patron): ")
        match user_type:
            case 'librarian':
                user = Librarian()
            case 'user':
                user = Patron()
            case defualt:
                print("Wrong user type!")
            
    while True:
        print("1. Browse catalog\n2. Check out an item\n3. Return an item\n4. Exit")
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                user.browse_catalog()
            case 2:
                item_type = input("Enter the type of item you wish to check out (book/magazine/cd): ")
                title = input("Enter the title of the item you wish to check out: ")
                match item_type:
                    case 'book':
                        author = input("Enter the author of the book: ")
                        item = Book(title, author)
                    case 'magazine':
                        issue = input("Enter the issue number of the magazine: ")
                        publisher = input("Enter the publisher of the magazine: ")
                        item = Magazine(title, issue, publisher)
                    case 'cd':
                        title = input("Enter the title of the CD: ")
                        artist = input("Enter the artist of the CD: ")
                        item = CD(title, artist)
                    case default:
                        print("Invalid choice!")
                        continue
                user.check_out_item(item)
            case 3:
                item_type = input("Enter the type of item you wish to return (book/magazine/cd):")
                title = input("Enter the title of the item you wish to return: ")
                match item_type:
                    case 'book':
                        author = input("Enter the author of the book: ")
                        item = Book(title, author)
                    case'magazine':
                        issue = input("Enter the issue number of the magazine: ")
                        publisher = input("Enter the publisher of the magazine: ")
                        item = Magazine(title, issue, publisher)
                    case 'cd':
                        title = input("Enter the title of the CD: ")
                        artist = input("Enter the artist of the CD: ")
                        item = CD(title, artist)
                    case default:
                        print("Invalid choice!")
                        continue
                user.return_item(item)
            case 4:
                print("Exiting...")
                break
            case default:
                print("Invalid choice!")

if __name__ == "__main__":
    main()