from enums.equipment_slot import EquipmentSlot

class Equipment:
    def __init__(self, name, slot):
        self.name = name
        if isinstance(slot, EquipmentSlot):
            self.slot = slot
        else:
            raise ValueError("Invalid slot type.")