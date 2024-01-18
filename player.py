
from enum import Enum
from typing import List

from pawn import Pawn, PawnState, PawsnColor


class PlayerState(Enum):
    """Player state enumeration."""
    PLAYING = 0
    IDLE = 1
    DONE = 2

class Player:
    """Player class."""
    def __init__(self, color: PawsnColor, pawns: List[Pawn]):
        """Constructor."""
        self.color = color
        self.pawns = [p for p in pawns if p.color == color]
        self.active = False

    def __str__(self):
        """String representation."""
        return f"Player({self.color}, {len(self.pawns)}, {self.active})"
    
    def __repr__(self):
        """String representation."""
        return str(self)
    
    def in_stock_count(self):
        """Count pawns in stock."""
        return len([p for p in self.pawns if p.is_in_stock()])
    
    def in_goal_count(self):
        """Count pawns in goal."""
        return len([p for p in self.pawns if p.is_finished()])
    
    def is_finished(self):
        """Check if player is finished."""
        return self.in_goal_count() == 4
    
    def has_pawn_at_start(self):
        """Check if player has pawn at start."""
        return len([p for p in self.pawns if p.get_relative_position() == 0 and p.state == PawnState.MOVING]) > 0
    
    def find_pawn(self, pawn_state: PawnState):
        """Find pawn by state."""
        return [p for p in self.pawns if p.state == pawn_state][0]
    
    def moving_count(self):
        """Count pawns moving."""
        return len([p for p in self.pawns if p.is_moving()])
    
    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def is_actve(self):
        """Roll dice."""
        import random
        return random.randint(1,6)
    
    def status(self):
        """Player status."""
        if self.in_stock_count() == 4:
            return PlayerState.IDLE
        
        if self.in_goal_count() < 4 and self.moving_count() == 0:
            return PlayerState.IDLE
        
        if self.in_goal_count() < 4 and self.moving_count() > 0:
            return PlayerState.PLAYING
        
        if self.in_goal_count() == 4:
            return PlayerState.DONE

        return PlayerState.PLAYING
        
class Players:
    def __init__(self, pawns: List[Pawn]):
        """Constructor."""
        self.players = [Player(color, pawns) for color in PawsnColor]
        self.active_index = 0
        self.players[self.active_index].set_active()

    def get_current_player(self):
        """Get current player."""
        return self.players[self.active_index]
    
    def next_player(self):
        """Get next player."""
        self.active_index = (self.active_index + 1) % len(self.players)
        self.players[self.active_index].set_active()
        return self.get_current_player()
    
    def set_all_inactive(self):
        """Set all players inactive."""
        for p in self.players:
            p.set_inactive()

    def is_game_finished(self):
        """Check if game is finished."""
        won_players = [p for p in self.players if p.status() == PlayerState.DONE]
        if len(won_players) > 0:
            print(f"Player {won_players[0].color} won the game")
            return True
        else:
            return False