class Furniture:
    def __init__(self, name, style, material, price):
        self.name = name
        self.style = style
        self.material = material
        self.price = price
        
    def __str__(self):
        return f"{self.name} - Style: {self.style}, Material: {self.material}, Price: ${self.price}"