from enums.equipment_slot import EquipmentSlot

class Equipment:
    def __init__(self, name, slot):
        self.name = name
        if isinstance(slot, EquipmentSlot):
            self.slot = slot
        else:
            raise ValueError("Invalid slot type.")
        
    def __str__(self):
        return f"{self.name} (equipped in slot: {self.slot})"
    
class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __str__(self):
        return f"{self.name}: {self.value}"
    
class Appearance:
    def __init__(self, hair_color, eye_color, skin_color):
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.skin_color = skin_color

    def __str__(self):
        return f"Hair color: {self.hair_color}, Eye color: {self.eye_color}, Skin color: {self.skin_color}"

class Ability:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"