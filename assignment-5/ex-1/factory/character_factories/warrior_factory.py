from factory.character_factory import CharacterFactory
from characters.warrior import Warrior

class WarriorFactory(CharacterFactory):
    def create_character(self, name):
        appearance = {}
        abilities = []
        equipment = []
        attributes = {}
    
        return Warrior(name, appearance, abilities, equipment, attributes)