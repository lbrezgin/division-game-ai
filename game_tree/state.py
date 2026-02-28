from dataclasses import dataclass

from player import Player

@dataclass(frozen=True)
class State:
    """
    Immutable representation of a game state.

    The class is frozen to guarantee immutability.

    Attributes:
        number (int): Current numeric value of the game.
        human_points (int): Accumulated points of the human player.
        computer_points (int): Accumulated points of the computer player.
        turn (Player): Player whose turn it is to move.
    """
    number: int
    human_points: int
    computer_points: int
    turn: Player
