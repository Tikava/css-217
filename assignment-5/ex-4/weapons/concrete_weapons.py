from weapons.weapon import Weapon

class Staff(Weapon):
    def __init__(self):
        super().__init__('Staff', damage=10, speed=15, range=10)
        
class Bow(Weapon):
    def __init__(self):
        super().__init__("Bow", damage=20, speed=25, range=30)

class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword", damage=30, speed=20, range=10)
