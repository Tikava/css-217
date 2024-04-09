class MazeDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_maze(self):
        self.builder.build_maze()
        self.builder.build_rooms()
        self.builder.build_walls()
        self.builder.build_doors()

    def get_maze(self):
        return self.builder.get_maze()
