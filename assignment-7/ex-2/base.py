class DocumentManagement:
    """
    This class represents the actual document storage and management system.
    """

    def __init__(self):
        self.documents = {}

    def upload_document(self, filename, content):
        self.documents[filename] = {"content": content}

    def edit_document(self, filename, new_content):
        if filename in self.documents:
            self.documents[filename]["content"] = new_content
        else:
            raise FileNotFoundError(f"Document '{filename}' not found.")

    def download_document(self, filename):
        if filename in self.documents:
            return self.documents[filename]["content"]
        else:
            raise FileNotFoundError(f"Document '{filename}' not found.")

    def search_documents(self, query):
        results = []
        for filename, data in self.documents.items():
            if query.lower() in filename.lower() or query.lower() in data["content"].lower():
                results.append(filename)
        return results