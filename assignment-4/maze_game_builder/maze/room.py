class Room:
    def __init__(self, room_no):
        self.room_no = room_no
        self.sides = {}

    def set_side(self, direction, wall):
        self.sides[direction] = wall