from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def browse_catalog(self):
        pass
    
    @abstractmethod
    def check_out_item(self, item):
        pass
    
    @abstractmethod
    def return_item(self, item):
        pass