from enum import Enum

from enums.equipment_slot import EquipmentSlot

class EquipmentOptions(Enum):
    WARRIOR = [
        ("Sword", EquipmentSlot.WEAPON),
        ("Axe", EquipmentSlot.WEAPON),
        ("Hammer", EquipmentSlot.WEAPON),
        ("Shield", EquipmentSlot.OFF_HAND),
        ("Plate Armor", EquipmentSlot.CHEST),
        ("Chainmail", EquipmentSlot.CHEST),
        ("Helmet", EquipmentSlot.HEAD),
        ("Greaves", EquipmentSlot.LEGS)
    ]
    MAGE = [
        ("Staff", EquipmentSlot.WEAPON),
        ("Wand", EquipmentSlot.WEAPON),
        ("Robe", EquipmentSlot.CHEST),
        ("Cloak", EquipmentSlot.BACK),
        ("Spellbook", EquipmentSlot.OFF_HAND),
        ("Amulet", EquipmentSlot.ACCESSORY)
    ]
    ARCHER = [
        ("Bow", EquipmentSlot.WEAPON),
        ("Crossbow", EquipmentSlot.WEAPON),
        ("Quiver", EquipmentSlot.BACK),
        ("Leather Armor", EquipmentSlot.CHEST),
        ("Boots", EquipmentSlot.LEGS),
        ("Gloves", EquipmentSlot.HANDS),
        ("Hood", EquipmentSlot.HEAD)
    ]
