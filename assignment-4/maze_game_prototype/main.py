from maze_game import MazeGame

def main():
    maze_prototype = MazeGame.create_maze()
    maze_clone = maze_prototype.clone()
    print("Maze created successfully!")

if __name__ == "__main__":
    main()
