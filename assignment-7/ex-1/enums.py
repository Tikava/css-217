from enum import Enum

class SupportType(Enum):
    HARDWARE = 1
    SOFTWARE = 2
    NETWORK = 3
    
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
