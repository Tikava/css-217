from factory.character_factory import CharacterFactory
from characters.mage import Mage

class MageFactory(CharacterFactory):
    def create_character(self, name):
        appearance = {}
        abilities = []
        equipment = []
        attributes = {}
    
        return Mage(name, appearance, abilities, equipment, attributes)
    