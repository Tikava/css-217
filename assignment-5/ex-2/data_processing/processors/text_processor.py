from data_processing.processors.base_processor import DataProcessor

class TextProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        print("Processing text:", self.data.content.text)

class TextDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        return TextProcessor(data)