import random

from state import State

class WrongDivider(Exception):
    pass

class IllegalMove(Exception):
    pass

class GameRules:
    def __init__(
            self, 
            from_number: int, 
            to_number: int,
            dividers: tuple[int,...], 
            terminal_number: int,
            depth: int
        ) -> None:
        self.from_number = from_number
        self.to_number = to_number
        self.dividers = dividers
        self.terminal_number = terminal_number
        self.depth = depth

    def ai_move(self, state: State, divider: int) -> State:
        if divider not in self.dividers:
            raise WrongDivider 
        if state.number % divider != 0:
            raise IllegalMove

        new_number = state.number // divider
        new_state = State(new_number, state.human_points, state.ai_points)
        
        if new_number % 2 == 0:
            new_state.human_points -= 1
        else:
            new_state.ai_points += 1

        return new_state
    
    def human_move(self, state: State, divider: int) -> State:
        if divider not in self.dividers:
            raise WrongDivider 
        if state.number % divider != 0:
            raise IllegalMove

        new_number = state.number // divider
        new_state = State(new_number, state.human_points, state.ai_points)
        
        if new_number % 2 == 0:
            new_state.ai_points -= 1
        else:
            new_state.human_points += 1
        return new_state

    @staticmethod
    def heuristic(state: State) -> int:
        # Simple implementation for now
        return state.ai_points - state.human_points

    def is_legal(self, state: State, divider: int) -> bool:
        return divider in self.dividers and state.number % divider == 0

    def is_game_over(self, state: State) -> bool:
        return state.number <= self.terminal_number
    
    def generate_random_number(self) -> int:
        valid = [x for x in range(self.from_number, self.to_number + 1) if x % 12 == 0]
        return random.choice(valid)