from abc import ABC, abstractmethod

class MazeBuilder(ABC):
    @abstractmethod
    def build_maze(self):
        pass

    @abstractmethod
    def build_rooms(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def get_maze(self):
        pass
