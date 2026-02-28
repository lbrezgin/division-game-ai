import random
from dataclasses import dataclass

from state import State
from player import Player

@dataclass(frozen=True)
class RulesConfig:
    """
    A class representing a configuration parameters defining
    the game rules and search constraints.

    Attributes:
        lower_bound (int): Minimum value used for initial number generation.
        upper_bound (int): Maximum value used for initial number generation.
        divisors (tuple[int,...]): Allowed divisors for valid moves.
        terminal_limit (int): Game is terminal when state.number <= this value.
        max_depth (int): Maximum minimax search depth.
        alfa_beta_optimization (bool): Set True if you want to optimize minimax algorithm
                                       using alfa and beta values.
    """
    lower_bound: int
    upper_bound: int
    divisors: tuple[int,...]
    terminal_limit: int
    max_depth: int
    alfa_beta_optimization: bool


class GameRules:
    """
    A class representing the core game mechanics and evaluation logic.

    Attributes:
        cfg (RulesConfig): Configuration object containing generation bounds,
                           divisors, terminal conditions, and search depth parameters.
    """
    def __init__(self, config: RulesConfig) -> None:
        self.cfg = config

    def start_number_generator(self, count: int = 5) -> list[int]:
        """
        Generates a sorted list of unique starting numbers.

        Parameters:
            count (int): Number of starting numbers to generate. Defaults to 5.

        Returns:
            list[int]: Sorted list of valid starting numbers.
        """
        numbers = set()

        while len(numbers) < count:
            n = random.randint(self.cfg.lower_bound, self.cfg.upper_bound)

            if n % 12 == 0:  # divisible by 2,3,4
                numbers.add(n)

        return sorted(numbers)

    def is_terminal(self, state: State) -> bool:
        """
        Determines whether the given state is terminal.

        A state is considered terminal if:
            - the number is less than or equal to the terminal limit, or
            - the number is not divisible by any allowed divisor.

        Parameters:
            state (State): Current game state.

        Returns:
            bool: True if the state is terminal, False otherwise.
        """
        if state.number <= self.cfg.terminal_limit:
            return True

        for d in self.cfg.divisors:
            if state.number % d == 0:
                return False

        return True

    @staticmethod
    def apply_move(state: State, divisor: int) -> State:
        """
        Applies a move to the given state and returns a new state.

        Parameters:
            state (State): Current game state
            divisor (int): Divisor used to generate the next state.

        Returns:
            State: New game state after applying the move.
        """
        new_number = state.number // divisor

        even = (new_number % 2 == 0)

        human_points = state.human_points
        computer_points = state.computer_points

        if state.turn == Player.HUMAN:
            if even:
                computer_points -= 1
            else:
                human_points += 1
            next_turn = Player.COMPUTER

        else:
            if even:
                human_points -= 1
            else:
                computer_points += 1
            next_turn = Player.HUMAN

        return State(new_number, human_points, computer_points, next_turn)

    @staticmethod
    def evaluate(state: State) -> int:
        """
        Evaluates the given state from the computer's perspective.

        Parameters:
            state (State): Current game state.

        Returns:
            int: Heuristic score of the state.
        """
        return state.computer_points - state.human_points
