from copy import deepcopy

class MazePrototype:
    def __init__(self):
        self.rooms = {}

    def clone(self):
        return deepcopy(self)

    def add_room(self, room):
        self.rooms[room.room_no] = room

    def room_no(self, r):
        return self.rooms.get(r)
