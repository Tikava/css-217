from enums.ability_options import AbilityOptions
from enums.apperance_options import AppearanceOptions
from enums.equipment_options import EquipmentOptions
from customization.character_customization import Attribute, Equipment, Appearance, Ability

def customize_appearance(character):
    print("Customizing appearance:")
    hair_color_options = AppearanceOptions['HAIR_COLOR'].value
    eye_color_options = AppearanceOptions['EYE_COLOR'].value
    skin_color_options = AppearanceOptions['SKIN_COLOR'].value

    hair_color = input(f"Select hair color ({', '.join(hair_color_options)}): ").strip()
    while hair_color not in hair_color_options:
        print("Invalid choice. Please select from the available options.")
        hair_color = input(f"Select hair color ({', '.join(hair_color_options)}): ").strip()

    eye_color = input(f"Select eye color ({', '.join(eye_color_options)}): ").strip()
    while eye_color not in eye_color_options:
        print("Invalid choice. Please select from the available options.")
        eye_color = input(f"Select eye color ({', '.join(eye_color_options)}): ").strip()

    skin_color = input(f"Select skin color ({', '.join(skin_color_options)}): ").strip()
    while skin_color not in skin_color_options:
        print("Invalid choice. Please select from the available options.")
        skin_color = input(f"Select skin color ({', '.join(skin_color_options)}): ").strip()

    character.appearance = Appearance(hair_color, eye_color, skin_color)


def customize_abilities(character):
    print("Customizing abilities:")
    class_name = (type(character).__name__).upper()
    abilities = AbilityOptions[class_name].value
    for idx, ability in enumerate(abilities, start=1):
        print(f"{idx}. {ability}")
    choice = input("Select ability: ")
    if choice.isdigit() and int(choice) in range(1, len(abilities) + 1):
        character.abilities.append(Ability(abilities[int(choice) - 1]))
    else:
        print("Invalid choice. No ability selected.")
        
def customize_equipment(character):
    print("Customizing equipment:")
    class_name = character.__class__.__name__.upper()
    equipment_options = EquipmentOptions[class_name].value

    for idx, (item, slot) in enumerate(equipment_options, start=1):
        print(f"{idx}. {item} ({slot.value})")

    choice = input("Select equipment: ")
    if choice.isdigit() and int(choice) in range(1, len(equipment_options) + 1):
        selected_item, selected_slot = equipment_options[int(choice) - 1]
        equipment = Equipment(selected_item, selected_slot)
        character.equipment.append(equipment)
    else:
        print("Invalid choice. No equipment selected.")

def customize_attributes(character):
    print("Customizing attributes:")
    attributes = []
    for attribute_name in ["attack", "defense", "health"]:
        value = input(f"Enter {attribute_name.capitalize()}: ")
        try:
            value = int(value)
            attributes.append(Attribute(attribute_name, value))
        except ValueError:
            print("Invalid input. Attribute not changed.")
    
    character.attributes = attributes
