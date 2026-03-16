from dataclasses import dataclass

@dataclass
class Metrics:
    """
    Stores performance metrics for the game AI search process.

    Attributes
        generated_node_count (int): Total number of nodes generated in the search tree during the whole game.
        evaluated_node_count (int): Total number of nodes that were evaluated by the heuristic function during the whole game.
        time_used_to_make_ai_move (float): Time in seconds that the AI used to compute the current move.
    """
    generated_node_count: int = 0
    evaluated_node_count: int = 0
    time_used_to_make_ai_move: float = 0