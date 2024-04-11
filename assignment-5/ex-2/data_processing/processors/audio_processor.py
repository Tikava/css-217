from base_processor import DataProcessor

class AudioProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        print("Processing audio:", self.data.content.audio_data)

class AudioDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        return AudioProcessor(data)