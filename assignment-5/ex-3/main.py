from factory.factory_impl import (
    ModernWoodFactory, ModernMetalFactory, ModernGlassFactory,
    TraditionalWoodFactory, TraditionalMetalFactory, TraditionalGlassFactory,
    IndustrialWoodFactory, IndustrialMetalFactory, IndustrialGlassFactory
)
from furniture_creator import FurnitureCreator

def main():
    print("Welcome to the Furniture Factory!")

    material = prompt_user("Select material (wood, metal, glass): ", ["wood", "metal", "glass"])
    style = prompt_user("Select style (modern, traditional, industrial): ", ["modern", "traditional", "industrial"])

    factory = None
    if style == "modern":
        if material == "wood":
            factory = ModernWoodFactory()
        elif material == "metal":
            factory = ModernMetalFactory()
        elif material == "glass":
            factory = ModernGlassFactory()
    elif style == "traditional":
        if material == "wood":
            factory = TraditionalWoodFactory()
        elif material == "metal":
            factory = TraditionalMetalFactory()
        elif material == "glass":
            factory = TraditionalGlassFactory()
    elif style == "industrial":
        if material == "wood":
            factory = IndustrialWoodFactory()
        elif material == "metal":
            factory = IndustrialMetalFactory()
        elif material == "glass":
            factory = IndustrialGlassFactory()

    if factory:
        create_and_display_furniture(factory)
    else:
        print("Invalid selection. Please try again.")

def prompt_user(prompt, options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in options:
            return user_input
        print("Invalid input. Please try again.")

def create_and_display_furniture(factory):
    creator = FurnitureCreator()
    creator.set_factory(factory)

    chair = creator.create_chair()
    table = creator.create_table()
    sofa = creator.create_sofa()

    print("\nFurniture created by", type(factory).__name__)
    print("Chair:", chair)
    print("Table:", table)
    print("Sofa:", sofa)

if __name__ == "__main__":
    main()
