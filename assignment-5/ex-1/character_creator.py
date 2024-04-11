class CharacterCreator:
    def __init__(self, factory):
        self.factory = factory
        
    def set_factory(self, factory):
        self.factory = factory
    
    def create_character(self, name):
        return self.factory.create_character(name)