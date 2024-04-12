from factory.furniture_factory import FurnitureFactory

class FurnitureCreator:
    def __init__(self):
        self.factory = None

    def set_factory(self, factory: FurnitureFactory):
        self.factory = factory

    def create_chair(self):
        if self.factory:
            return self.factory.create_chair()
        else:
            raise ValueError("Factory not set")

    def create_table(self):
        if self.factory:
            return self.factory.create_table()
        else:
            raise ValueError("Factory not set")

    def create_sofa(self):
        if self.factory:
            return self.factory.create_sofa()
        else:
            raise ValueError("Factory not set")
