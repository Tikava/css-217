class CharacterCreator:
    def set_factory(self, factory):
        self.factory = factory
        
    def create_character(self, name, health, mana):
        character = self.factory.create_character(name, health, mana)
        return character