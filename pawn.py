from enum import Enum
from typing import List

class PawnState(Enum):
    """Pawn state enumeration."""
    STOCK = 0
    MOVING = 1
    FINISHED = 2

class PawsnColor(Enum):
    """Pawn color enumeration."""
    RED = 0
    BLUE = 1
    YELLOW = 2
    GREEN = 3

class Pawn: 
    """Pawn class."""
    def __init__(self, color):
        """Constructor."""
        self.color = color
        self.state = PawnState.STOCK
        self.position = 0

    def __str__(self):
        """String representation."""
        return f"Pawn({self.color}, {self.state}, {self.get_relative_position()})"

    def __repr__(self):
        """String representation."""
        return str(self)
    
    def start_moving(self):
        """Start moving pawn."""
        print(f"Pawn {self.color} starts moving")
        self.state = PawnState.MOVING
        self.position = 0
        return self

    def move(self, steps):
        """Move pawn."""
        self.position += steps
        if self.position > 40:
            print(f"Pawn {self.color} is finished")
            self.state = PawnState.FINISHED
        else:
            print(f"Pawn {self.color} is at position {self.get_position()}")
            self.state = PawnState.MOVING

    def reset(self):
        """Reset pawn."""
        self.state = PawnState.STOCK
        self.position = 0
        print(f"Pawn {self.color} is back to stock")

    def is_in_stock(self):
        """Check if pawn is at home."""
        return self.state == PawnState.STOCK

    def is_finished(self):
        """Check if pawn is finished."""
        return self.state == PawnState.FINISHED

    def is_moving(self):
        """Check if pawn is moving."""
        return self.state == PawnState.MOVING

    def get_relative_position(self):
        """Get position."""
        return self.position
    
    def get_position(self) -> int:
        return self.position + self.color.value * 10

    def get_color(self):
        """Get color."""
        return self.color

    def get_state(self):
        """Get state."""
        return self.state
    
def create_pawns() -> List[Pawn]:
    """Create all default Pawns.

    Yields:
        _type_: Pawn
    """
    return [Pawn(color) for color in PawsnColor for loop in range(4)]