from dataclasses import dataclass

@dataclass
class Metrics:
    """
    Stores performance metrics for the game AI search process.

    Attributes
        generated_node_count (int): Total number of nodes generated in the search tree during the whole game.
        evaluated_node_count (int): Total number of nodes that were evaluated by the heuristic function during the whole game.
        total_ai_move_time (float): Total time in seconds that the AI spent computing all moves in the current game.
        ai_move_count (int): Number of AI moves made in the current game.
    """
    generated_node_count: int = 0
    evaluated_node_count: int = 0
    total_ai_move_time: float = 0
    ai_move_count: int = 0

    @property
    def average_ai_move_time(self) -> float:
        """Average time in seconds used to compute one AI move in the current game."""
        if self.ai_move_count == 0:
            return 0.0
        return self.total_ai_move_time / self.ai_move_count
