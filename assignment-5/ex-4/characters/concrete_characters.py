from characters.character import Character

class Knight(Character):
    def __init__(self, name, weapon, health, mana):
        super().__init__(name, type='Combat', weapon=weapon, health=health, mana=mana)
        
class Wizard(Character):
    def __init__(self, name, weapon, health, mana):
        super().__init__(name, type='Magic', weapon=weapon, health=health, mana=mana)
        
class Archer(Character):
    def __init__(self, name, weapon, health, mana):
        super().__init__(name, type='Combat', weapon=weapon, health=health, mana=mana)