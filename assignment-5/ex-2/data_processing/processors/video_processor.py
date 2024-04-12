from data_processing.processors.base_processor import DataProcessor

class VideoProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        print("Processing video:", self.data.content.video_data)

class VideoDataProcessor(DataProcessor):
    def create_data_processor(self, data):
        return VideoProcessor(data)