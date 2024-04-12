from data_processing.processors.base_processor import DataProcessor
from data_processing.data_storage import DataStorage

class TextProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        DataStorage().store_article(self.data.content["title"], 
                ", ".join(self.data.content["authors"]), 
                self.data.content["publicationYear"], 
                self.data.content["abstract"], 
                self.data.content["doi"], 
                self.data.content["journal"], 
                self.data.content["volume"], 
                self.data.content["issue"], 
                self.data.content["pages"], 
                ", ".join(self.data.content["keywords"]))
        print("Text saved:", self.data)

class TextDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        return TextProcessor(data)