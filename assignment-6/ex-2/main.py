from character import BasicCharacter
from decorator import DoubleDamageDecorator, FireballDecorator, InvisibilityDecorator

def main():
    character = BasicCharacter()
    print(character.get_description())  
    print(character.get_damage()) 

    double_damage_decorator = DoubleDamageDecorator(character)
    fireball_decorator = FireballDecorator(character)
    invisibility_decorator = InvisibilityDecorator(character)

    print(double_damage_decorator.get_description())  
    print(double_damage_decorator.get_damage())      
    
    print(fireball_decorator.get_description()) 
    print(fireball_decorator.get_damage())       

    print(invisibility_decorator.get_description())  
    print(invisibility_decorator.get_damage())      

    # Combining
    double_fireball_character = DoubleDamageDecorator(FireballDecorator(character))
    print(double_fireball_character.get_description())  
    print(double_fireball_character.get_damage())      
    
    invisibility_double_fireball_character = InvisibilityDecorator(double_fireball_character)
    print(invisibility_double_fireball_character.get_description())  
    print(invisibility_double_fireball_character.get_damage())      

if __name__ == "__main__":
    main()