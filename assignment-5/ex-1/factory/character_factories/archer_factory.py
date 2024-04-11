from factory.character_factory import CharacterFactory
from characters.archer import Archer

class ArcherFactory(CharacterFactory):
    def create_character(self, name):
        appearance = {}
        abilities = []
        equipment = []
        attributes = {}
        
        return Archer(name, appearance, abilities, equipment, attributes)