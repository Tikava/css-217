from maze_prototype import MazePrototype
from room import Room
from wall import Wall, DoorWall
from enums import Direction

class MazeGame:
    @staticmethod
    def create_maze():
        maze_prototype = MazePrototype()

        for room_number in range(1, 3):
            room = Room(room_number)
            for direction in Direction:
                room.set_side(direction, Wall())
            maze_prototype.add_room(room)

        door = DoorWall(maze_prototype.rooms[1], maze_prototype.rooms[2])
        maze_prototype.rooms[1].set_side(Direction.EAST, door)
        maze_prototype.rooms[2].set_side(Direction.WEST, door)

        return maze_prototype
