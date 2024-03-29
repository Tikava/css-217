import models

def main():
    librarian = models.Librarian()
    
    while True:
        print("1. Browse catalog\n2. Check out an item\n3. Return an item\n4. Exit")
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                librarian.browse_catalog()
            case 2:
                item_type = input("Enter the type of item you wish to check out (book/magazine/cd): ")
                title = input("Enter the title of the item you wish to check out: ")
                match item_type:
                    case 'book':
                        author = input("Enter the author of the book: ")
                        item = models.Book(title, author)
                    case 'magazine':
                        issue = input("Enter the issue number of the magazine: ")
                        publisher = input("Enter the publisher of the magazine: ")
                        item = models.Magazine(title, issue, publisher)
                    case 'cd':
                        title = input("Enter the title of the CD: ")
                        artist = input("Enter the artist of the CD: ")
                        item = models.CD(title, artist)
                    case default:
                        print("Invalid choice!")
                        continue
                librarian.check_out_item(item)
            case 3:
                item_type = input("Enter the type of item you wish to return (book/magazine/cd):")
                title = input("Enter the title of the item you wish to return: ")
                match item_type:
                    case 'book':
                        author = input("Enter the author of the book: ")
                        item = models.Book(title, author)
                    case'magazine':
                        issue = input("Enter the issue number of the magazine: ")
                        publisher = input("Enter the publisher of the magazine: ")
                        item = models.Magazine(title, issue, publisher)
                    case 'cd':
                        title = input("Enter the title of the CD: ")
                        artist = input("Enter the artist of the CD: ")
                        item = models.CD(title, artist)
                    case default:
                        print("Invalid choice!")
                        continue
                librarian.return_item(item)
            case 4:
                print("Exiting...")
                break
            case default:
                print("Invalid choice!")

if __name__ == "__main__":
    main()