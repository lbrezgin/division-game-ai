import math

from state import State
from node import Node

AI_ROLE = "AI"
HUMAN_ROLE = "HUMAN"

class GameTree:
    def __init__(self, root: Node):
        self.root = root

    def minimax(self, current_node: Node, depth: int, maximizing_player: bool) -> int:
        if depth == 0 or self._is_game_over(current_node):
            return self._heuristic(current_node)

        if maximizing_player:
            max_eval = -math.inf
            children = self._generate_children(parent_node=current_node, role=AI_ROLE)
            for child in children:
                evalu = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, evalu)
            return max_eval
        else:
            min_eval = +math.inf
            children = self._generate_children(parent_node=current_node, role=HUMAN_ROLE)
            for child in children:
                evalu = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, evalu)
            return min_eval

    # def alfa_beta(self):

    @staticmethod
    def _heuristic(node: Node) -> int:
        return node.state.ai_points - node.state.human_points

    @staticmethod
    def _is_game_over(node: Node) -> bool:
        return node.state.number <= 10

    def _generate_children(self, parent_node: Node, role: str) -> list[Node]:
        children = []
        for devisor in range(2, 5):
            if parent_node.state.number % devisor == 0:
                new_number = int(parent_node.state.number / devisor)
                new_state = State(number=new_number)
                new_node = Node(parent_node, new_state)
                self._redistribute_points(parent_node, new_node, role)
                children.append(new_node)
        return children

    @staticmethod
    def _redistribute_points(parent_node: Node, new_node: Node, role: str) -> Node:
        if new_node.state.number % 2 == 0:
            if role == AI_ROLE:
                new_node.state.human_points = parent_node.state.human_points - 1
                new_node.state.ai_points = parent_node.state.ai_points
            elif role == HUMAN_ROLE:
                new_node.state.ai_points = parent_node.state.ai_points - 1
                new_node.state.human_points = new_node.state.human_points
        else:
            if role == AI_ROLE:
                new_node.state.ai_points = parent_node.state.ai_points + 1
                new_node.state.human_points = parent_node.state.human_points
            elif role == HUMAN_ROLE:
                new_node.state.human_points = parent_node.state.human_points + 1
                new_node.state.ai_points = parent_node.state.ai_points
        return new_node
