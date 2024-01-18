from typing import List
from dice import MAX_DICE, dice_roll
from pawn import Pawn, PawnState
from player import PlayerState, Players


def play_round(players: Players, pawns: List[Pawn], next_player: bool = True):
    if(next_player):
        players.next_player()

    step = dice_roll()    
    current_player = players.get_current_player()

    if(step == MAX_DICE):
        if(current_player.in_stock_count() > 0):
            if current_player.has_pawn_at_start() == False:
                new_pawn = current_player.find_pawn(PawnState.STOCK).start_moving()
                move_pawn(new_pawn, pawns, dice_roll())
            else:
                move_pawn([p for p in current_player.pawn if p.get_relative_position() == 0 and p.state == PawnState.MOVING][0], pawns, step)
        else:
            if(current_player.moving_count() > 0):
                selected_pawn = current_player.find_pawn(PawnState.MOVING)
                move_pawn(selected_pawn, pawns, step)
            else:
                print("stop")
    elif(current_player.moving_count() > 0):
        selected_pawn = current_player.find_pawn(PawnState.MOVING)
        move_pawn(selected_pawn, pawns, step)
    else:
        print(f"Player {current_player.color} has no pawns moving")
            
    
            
def move_pawn(pawn: Pawn, pawns: List[Pawn], steps: int):
    next_position: int = (pawn.get_position() + steps) % 40
    pawns_on_next_position = [p for p in pawns if p.get_position() == next_position and p.state == PawnState.MOVING] 
    if len(pawns_on_next_position) > 0:
        for remove_pawn in pawns_on_next_position:
            remove_pawn.reset()

    pawn.move(steps)


    

