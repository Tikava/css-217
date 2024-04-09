from director import MazeDirector
from builders.standard_maze_builder import StandardMazeBuilder

def main():
    builder = StandardMazeBuilder()
    director = MazeDirector(builder)
    director.construct_maze()
    maze = director.get_maze()
    print("Maze constructed successfully!")

if __name__ == "__main__":
    main()
