from dataclasses import dataclass

from state import State

@dataclass
class Node:
    """
    Game tree node.

    Attributes:
        state (State): Game state represented by this node.
        children (list[tuple[Node, int]]): List of child nodes
                                           paired with the move (divisor)
                                           that produced each child state.
    """
    state: State
    children: list[tuple['Node', int]]
