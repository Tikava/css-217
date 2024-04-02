from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def check_out(self):
        pass
    
    @abstractmethod
    def return_item(self):
        pass