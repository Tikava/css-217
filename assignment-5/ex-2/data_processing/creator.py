class DataProcessorCreator:
    def __init__(self, processor=None):
        self.processor = processor

    def set_processor(self, processor):
        self.processor = processor

    def process_data(self, data):
        if self.processor:
            data_processor = self.processor.create_data_processor(data)
            data_processor.process()
        else:
            print("No processor set!")
