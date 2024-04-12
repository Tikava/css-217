from factory.furniture_factory import FurnitureFactory
from furniture import Furniture

class ModernWoodFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Modern Wood Chair", "Modern", "Wood", 110.0)

    def create_table(self):
        return Furniture("Modern Wood Table", "Modern", "Wood", 135.0)

    def create_sofa(self):
        return Furniture("Modern Wood Sofa", "Modern", "Wood", 140.0)
    
class ModernMetalFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Modern Metal Chair", "Modern", "Metal", 120.0)

    def create_table(self):
        return Furniture("Modern Metal Table", "Modern", "Metal", 145.0)

    def create_sofa(self):
        return Furniture("Modern Metal Sofa", "Modern", "Metal", 150.0)
    
class ModernGlassFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Modern Glass Chair", "Modern", "Glass", 115.0)

    def create_table(self):
        return Furniture("Modern Glass Table", "Modern", "Glass", 140.0)

    def create_sofa(self):
        return Furniture("Modern Glass Sofa", "Modern", "Glass", 145.0)
    
class TraditionalWoodFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Traditional Wood Chair", "Traditional", "Wood", 95.0)

    def create_table(self):
        return Furniture("Traditional Wood Table", "Traditional", "Wood", 120.0)

    def create_sofa(self):
        return Furniture("Traditional Wood Sofa", "Traditional", "Wood", 125.0)
    
class TraditionalMetalFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Traditional Metal Chair", "Traditional", "Metal", 105.0)

    def create_table(self):
        return Furniture("Traditional Metal Table", "Traditional", "Metal", 130.0)

    def create_sofa(self):
        return Furniture("Traditional Metal Sofa", "Traditional", "Metal", 135.0)

class TraditionalGlassFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Traditional Glass Chair", "Traditional", "Glass", 100.0)

    def create_table(self):
        return Furniture("Traditional Glass Table", "Traditional", "Glass", 125.0)

    def create_sofa(self):
        return Furniture("Traditional Glass Sofa", "Traditional", "Glass", 130.0)
    
class IndustrialWoodFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Industrail Wood Chair", "Industrail", "Wood", 100.0)

    def create_table(self):
        return Furniture("Industrail Wood Table", "Industrail", "Wood", 125.0)

    def create_sofa(self):
        return Furniture("Industrail Wood Sofa", "Industrail", "Wood", 130.0)
    
class IndustrialMetalFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Industrail Metal Chair", "Industrail", "Metal", 110.0)

    def create_table(self):
        return Furniture("Industrail Metal Table", "Industrail", "Metal", 135.0)

    def create_sofa(self):
        return Furniture("Industrail Metal Sofa", "Industrail", "Metal", 140.0)
    
class IndustrialGlassFactory(FurnitureFactory):
    def create_chair(self):
        return Furniture("Industrail Glass Chair", "Industrail", "Glass", 105.0)

    def create_table(self):
        return Furniture("Industrail Glass Table", "Industrail", "Glass", 130.0)

    def create_sofa(self):
        return Furniture("Industrail Glass Sofa", "Industrail", "Glass", 135.0)
