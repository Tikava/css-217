import logging
from datetime import datetime

from utils import AuthenticationManager
from base import DocumentManagement

class DocumentManagementProxy:
    """
    This class acts as a proxy to the DocumentManagement system and enforces access control.
    """

    def __init__(self, users):
        self.auth_manager = AuthenticationManager(users) 
        self.document_management = DocumentManagement()
        self.logger = logging.getLogger(__name__)

    def login(self, username, password):
        session_token = self.auth_manager.login(username, password)
        return session_token

    def logout(self, session_token):
        self.auth_manager.logout(session_token)

    def is_authorized(self, session_token, required_roles):
        return self.auth_manager.is_authorized(session_token, required_roles)

    def upload_document(self, session_token, filename, content):
        if self.is_authorized(session_token, ["admin", "user"]):
            try:
                self.document_management.upload_document(filename, content)
                self.log_activity("upload", session_token, filename)
                print(f"Document '{filename}' uploaded successfully.")
            except Exception as e:
                print(f"Error uploading document: {e}")
        else:
            print("You must login first.")

    def search_documents(self, session_token, query):
        if self.auth_manager.is_authorized(session_token, ["admin", "user"]):
            results = self.document_management.search_documents(query)
            if results:
                self.log_activity("search", self.auth_manager.logged_in_users[session_token], query)
                print("Search results:")
                for result in results:
                    print(result)
            else:
                print("No documents found matching the search query.")
        else:
            print("You must login first.")
            
    def download_document(self, session_token, filename):
        if self.auth_manager.is_authorized(session_token, ["admin", "user"]):
            try:
                content = self.document_management.download_document(filename)
                self.log_activity("download", self.auth_manager.logged_in_users[session_token], filename)
                if content:
                    print(f"Content of '{filename}':\n{content}")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error downloading document: {e}")
        else:
            print("You must login first.")
    
    def edit_document(self, session_token, filename, new_content):
        if self.auth_manager.is_authorized(session_token, ["admin", "user"]):
            try:
                self.document_management.edit_document(filename, new_content)
                self.log_activity("edit", self.auth_manager.logged_in_users[session_token], filename)
                print(f"Document '{filename}' edited successfully.")
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"Error editing document: {e}")
        else:
            print("You must login first.")

    def log_activity(self, action, session_token, document):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.info(f"{timestamp} - {action} - {session_token} - {document}")
