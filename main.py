import time
from typing import List
from dice import dice_roll
from game import play_round
from pawn import Pawn, create_pawns
from player import Players

pawns: List[Pawn] = list(create_pawns())
players: Players = Players(pawns)

def main():
    play_round(players, pawns, False)
    rounds = 0
    while(players.is_game_finished() == False):
        play_round(players, pawns)
        rounds += 1

    print(f"Game finished after {rounds} rounds")

if __name__ == '__main__':
    main()