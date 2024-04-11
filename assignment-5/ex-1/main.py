def battle(character1, character2):
    print(f"{character1.name} vs {character2.name}!\n")

    while character1.attributes[2].value > 0 and character2.attributes[2].value > 0:
        damage = character1.attributes[0].value - character2.attributes[1].value
        if damage > 0:
            character2.attributes[2].value -= damage
            print(f"{character1.name} attacks {character2.name} for {damage} damage!")
        else:
            print(f"{character1.name}'s attack is ineffective against {character2.name}!")

            if damage <= 0 and character2.attributes[0].value - character1.attributes[1].value <= 0:
                print("The battle has reached a stalemate! Neither character can harm the other.")
                break

        if character2.attributes[2].value <= 0:
            print(f"{character2.name} has been defeated!")
            print("Character's customs: ", character2.__dict__)
            break

        damage = character2.attributes[0].value - character1.attributes[1].value
        if damage > 0:
            character1.attributes[2].value -= damage
            print(f"{character2.name} attacks {character1.name} for {damage} damage!")
        else:
            print(f"{character2.name}'s attack is ineffective against {character1.name}!")
            
            if damage <= 0 and character1.attributes[0].value - character2.attributes[1].value <= 0:
                print("The battle has reached a stalemate! Neither character can harm the other.")
                break

        if character1.attributes[2].value <= 0:
            print(f"{character1.name} has been defeated!")
            print("Character's customs: ", character1.__dict__)
            break

def main():
    from character_creator import CharacterCreator
    from factory.character_factories.warrior_factory import WarriorFactory
    from factory.character_factories.mage_factory import MageFactory
    from customization.customization_actions import customize_appearance, customize_abilities, customize_equipment, customize_attributes

    warrior_factory = WarriorFactory()
    mage_factory = MageFactory()

    creator = CharacterCreator(warrior_factory)

    warrior = creator.create_character("Warrior")
    mage = CharacterCreator(mage_factory).create_character("Mage")
    
    characters = [warrior, mage]
    for character in characters:
        customize_appearance(character)
        customize_abilities(character)
        customize_equipment(character)
        customize_attributes(character)
        print(f"Customization for {character.name} completed!")

    battle(warrior, mage)

if __name__ == "__main__":
    main()
