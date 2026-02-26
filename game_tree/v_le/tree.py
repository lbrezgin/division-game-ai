import math

from state import State
from node import Node
from rules import *

class GameTree:
    def __init__(self, root: Node, rules: GameRules):
        self.root = root
        self.rules = rules

    def best_move(self, state: State) -> int:
        best_value = -math.inf
        best_divider: int | None = None 

        for divider in self.rules.dividers:
            if self.rules.is_legal(state, divider):
                new_state = self.rules.ai_move(state, divider)
                new_node = Node(parent=None, state=new_state) # Parent is not important here

                value = self._minimax(new_node, self.rules.depth - 1, maximizing=False)
                
                if value > best_value:
                    best_value = value
                    best_divider = divider

        if best_divider is None:
            raise IllegalMove("AI don't have legal moves")
        return best_divider

    def _minimax(self, node: Node, depth: int, maximizing: bool) -> int:
        children = self._generate_children(node, maximizing)

        if depth == 0 or self.rules.is_game_over(node.state) or len(children) == 0:
            return self.rules.heuristic(node.state)

        if maximizing:
            max_eval = -math.inf

            for child in children:
                evalu = self._minimax(child, depth - 1, False)
                max_eval = max(max_eval, evalu)
            return max_eval
        else:
            min_eval = +math.inf

            for child in children:
                evalu = self._minimax(child, depth - 1, True)
                min_eval = min(min_eval, evalu)
            return min_eval
    
    def _generate_children(self, node: Node, maximizing: bool) -> list[Node]:
        children: list[Node] = []

        for divider in self.rules.dividers:
            if self.rules.is_legal(node.state, divider):
                if maximizing:
                    child = Node(parent=node, state=self.rules.ai_move(node.state, divider))
                else:
                    child = Node(parent=node, state=self.rules.human_move(node.state, divider))
                children.append(child)
        return children
    