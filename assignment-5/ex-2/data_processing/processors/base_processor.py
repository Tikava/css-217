from abc import ABC, abstractmethod

class DataProcessor(ABC):
    
    @abstractmethod
    def create_data_processor(self):
        pass