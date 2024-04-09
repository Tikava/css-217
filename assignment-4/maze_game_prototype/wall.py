class Wall:
    pass

class DoorWall(Wall):
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False
