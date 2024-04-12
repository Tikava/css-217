from factory.character_factory import CharacterFactory
from weapons.concrete_weapons import Sword, Staff, Bow
from characters.concrete_characters import Knight, Wizard, Archer

class KnightSwordFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Knight(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Sword()

class KnightBowFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Knight(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Bow()
    
class KnightStaffFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Knight(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Staff()
    
class WizardStaffFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Wizard(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Staff()
    
class WizardBowFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Wizard(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Bow()
    
class WizardSwordFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Wizard(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Sword()
    
class ArcherBowFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Archer(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Bow()
    
class ArcherSwordFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Archer(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Sword()
    
class ArcherStaffFactory(CharacterFactory):
    
    def create_character(self, name, health, mana):
        weapon = self.create_weapon()
        character = Archer(name, weapon, health, mana)
        return character
    
    def create_weapon(self):
        return Staff()