from abc import ABC, abstractmethod

class CharacterFactory(ABC):
    
    @abstractmethod
    def create_character(self, name):
        pass
    
    @abstractmethod
    def create_weapon(self):
        pass