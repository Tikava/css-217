from character_creator import CharacterCreator
import factory.concrete_factories as fct

def main():
    character_type = prompt_user("Select character type (knight, wizard, archer): ", ['knight', 'wizard', 'archer'])
    weapon = prompt_user("Select weapon (sword, bow, staff): ", ['sword', 'bow', 'staff'])
    
    factory = None
    if character_type == 'knight':
        if weapon == 'sword':
            factory = fct.KnightSwordFactory()
        elif weapon == 'bow':
            factory = fct.KnightBowFactory()
        elif weapon == 'staff':
            factory = fct.KnightStaffFactory()
    elif character_type == 'wizard':
        if weapon == 'sword':
            factory = fct.WizardSwordFactory()
        elif weapon == 'bow':
            factory = fct.WizardBowFactory()
        elif weapon == 'staff':
            factory = fct.WizardStaffFactory()
    elif character_type == 'archer':
        if weapon == 'sword':
            factory = fct.ArcherSwordFactory()
        elif weapon == 'bow':
            factory = fct.ArcherBowFactory()
        elif weapon == 'staff':
            factory = fct.ArcherStaffFactory()
            
    if factory:
        creator = CharacterCreator()
        creator.set_factory(factory)
        name = input("Enter character's name: ")
        health = int(input("Enter character's health: "))
        mana = int(input("Enter character's mana: "))
        character = creator.create_character(name, health, mana)
        print("Character created!", character)
    else:
        print('Invalid input. Try again.')
            

def prompt_user(prompt, options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return user_input
        print("Invalid input. Please try again.")
        
if __name__ == '__main__':
    main()