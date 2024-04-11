from abc import ABC, abstractmethod

class DataProcessor(ABC):
    
    @abstractmethod
    def create_dataprocessor(self):
        pass