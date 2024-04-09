from builders.maze_builder import MazeBuilder
from maze.maze import Maze
from maze.room import Room
from maze.wall import Wall
from enums import Direction

class StandardMazeBuilder(MazeBuilder):
    def __init__(self):
        self.maze = None

    def build_maze(self):
        self.maze = Maze()

    def build_rooms(self):
        for room_number in range(1, 3):
            self.maze.add_room(Room(room_number))

    def build_walls(self):
        for room in self.maze.rooms.values():
            for direction in Direction:
                room.set_side(direction, Wall())

    def build_doors(self):
        from maze.wall import DoorWall
        door = DoorWall(self.maze.rooms[1], self.maze.rooms[2])
        self.maze.rooms[1].set_side(Direction.EAST, door)
        self.maze.rooms[2].set_side(Direction.WEST, door)

    def get_maze(self):
        return self.maze
