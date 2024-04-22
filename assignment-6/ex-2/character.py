from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_damage(self):
        pass
    
class BasicCharacter(Character):
    def get_description(self):
        return "Basic Character"
    
    def get_damage(self):
        return 10