def battle(character1, character2):
    print(f"{character1.name} vs {character2.name}!\n")

    while character1.attributes['health'] > 0 and character2.attributes['health'] > 0:
        damage = character1.attributes['attack'] - character2.attributes['defense']
        if damage > 0:
            character2.attributes['health'] -= damage
            print(f"{character1.name} attacks {character2.name} for {damage} damage!")
        else:
            print(f"{character1.name}'s attack is ineffective against {character2.name}!")

        if character2.attributes['health'] <= 0:
            print(f"{character2.name} has been defeated!")
            break

        damage = character2.attributes['attack'] - character1.attributes['defense']
        if damage > 0:
            character1.attributes['health'] -= damage
            print(f"{character2.name} attacks {character1.name} for {damage} damage!")
        else:
            print(f"{character2.name}'s attack is ineffective against {character1.name}!")

        if character1.attributes['health'] <= 0:
            print(f"{character1.name} has been defeated!")
            break

def main():
    from character_creator import CharacterCreator
    from factory.character_factories.warrior_factory import WarriorFactory
    from factory.character_factories.archer_factory import ArcherFactory
    from factory.character_factories.mage_factory import MageFactory
    
    warrior_factory = WarriorFactory()
    mage_factory = MageFactory()
    archer_factory = ArcherFactory()

    creator = CharacterCreator(warrior_factory)

    warrior = creator.create_character("Warrior")
    mage = CharacterCreator(mage_factory).create_character("Mage")

    warrior.attributes = {"health": 100, "attack": 20, "defense": 10}
    mage.attributes = {"health": 80, "attack": 25, "defense": 5}

    battle(warrior, mage)
    
if __name__ == "__main__":
    main()    
