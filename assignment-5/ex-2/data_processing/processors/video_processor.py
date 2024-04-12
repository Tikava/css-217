from data_processing.processors.base_processor import DataProcessor
from data_processing.data_storage import DataStorage

class VideoProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        DataStorage().store_video(
            title=self.data.content['title'],
            description=self.data.content['description'],
            channel_title=self.data.content['channel_title'],
            published_at=self.data.content['published_at']
        )
        print("Video saved:", self.data)

class VideoDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        return VideoProcessor(data)
