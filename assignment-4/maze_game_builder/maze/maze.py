class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_no] = room

    def room_no(self, r):
        return self.rooms.get(r)