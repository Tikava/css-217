from data_processing.processors.base_processor import DataProcessor
from data_processing.data_storage import DataStorage

class AudioProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        DataStorage().store_audio(
            name=self.data.content['name'],
            artists=self.data.content['artists'],
            album=self.data.content['album'],
            preview_url=self.data.content['preview_url']
        )
        print("Audio saved:", self.data)

class AudioDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        return AudioProcessor(data)