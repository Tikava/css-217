from abc import ABC, abstractmethod
from character import Character

class CharacterDecorator(Character, ABC):
    def __init__(self, character):
        self._character = character
        
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_damage(self):
        pass
    
class DoubleDamageDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Double Damage"

    def get_damage(self):
        return self._character.get_damage() * 2
    
class FireballDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Fireball"

    def get_damage(self):
        return self._character.get_damage() + 20
    
class InvisibilityDecorator(CharacterDecorator):
    def get_description(self):
        return self._character.get_description() + " with Invisibility"

    def get_damage(self):
        return self._character.get_damage()