from proxy import DocumentManagementProxy

def main():
    
    users = {
            "admin": {"password": "admin123", "roles": ["admin"]},
            "user1": {"password": "user123", "roles": ["user"]},
            "user2": {"password": "user456", "roles": ["user"]},
        }
    dms_proxy = DocumentManagementProxy(users)
    session_token = None

    while True:
        print("\nMenu:")
        print("1. Login")
        print("2. Logout")
        print("3. Upload Document")
        print("4. Edit Document")
        print("5. Download Document")
        print("6. Search Documents")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            session_token = dms_proxy.login(username, password)
        elif choice == "2":
            if session_token:
                dms_proxy.logout(session_token)
                session_token = None
            else:
                print("You are not logged in.")
        elif choice == "3":
            if session_token:
                filename = input("Enter the name of the file to upload: ")
                content = input("Enter the content of the file: ")
                dms_proxy.upload_document(session_token, filename, content)
            else:
                print("You must login first.")
        elif choice == "4":
            if session_token:
                filename = input("Enter the name of the file to edit: ")
                new_content = input("Enter the new content of the file: ")
                dms_proxy.edit_document(session_token, filename, new_content)
            else:
                print("You must login first.")
        elif choice == "5":
            if session_token:
                filename = input("Enter the name of the file to download: ")
                content = dms_proxy.download_document(session_token, filename)
            else:
                print("You must login first.")
        elif choice == "6":
            if session_token:
                query = input("Enter your search query: ")
                dms_proxy.search_documents(session_token, query)
            else:
                print("You must login first.")
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()