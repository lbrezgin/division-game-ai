from typing import Optional

from .node import Node
from .rules import GameRules
from .player import Player
from .metrics import Metrics

class GameTree:
    """
    Implements game tree search for choosing optimal moves.

    Attributes:
        root (Node): Root node of the game tree.
        rules (GameRules): Rule set and evaluation logic used by the search.
        metrics (Metrics): Metrics related to game tree (generated, evaluated node count)
    """
    def __init__(
            self,
            root: Node,
            rules: GameRules,
            metrics: Metrics
    ) -> None:
        self.root = root
        self.rules = rules
        self.metrics = metrics

    def minimax_alpha_beta(
            self,
            node: Node,
            depth: int,
            alpha: float,
            beta: float
    ) -> tuple[int, Optional[int]]:
        """
        Runs minimax search with alpha-beta pruning from the given node.

        The computer is treated as the maximizing player, and the human as the
        minimizing player. Alpha-beta pruning reduces the number of explored
        nodes by cutting off branches that cannot influence the final decision.

        The method returns both the minimax value of the position and the best
        move (divisor) that achieves it for the current player.

        Parameters:
            node (Node): Node representing the current position to evaluate.
            depth (int): Remaining search depth. When it reaches 0, the position
                         is evaluated without further expansion.
            alpha (float): Best (highest) value found so far along the path for the
                           maximizing player.
            beta (float): Best (lowest) value found so far along the path for the
                          minimizing player.

        Returns:
            tuple[int, Optional[int]]: A pair of:
                - best_value: Minimax value of the position (after pruning).
                - best_move: Divisor (move) producing `best_value`. Returns None if
                             the node is terminal or `depth == 0`.
        """
        if self.rules.is_terminal(node.state) or depth == 0:
            self.metrics.evaluated_node_count += 1
            return self.rules.evaluate(node.state), None

        best_move = None
        if node.state.turn == Player.COMPUTER:  # computer is chosen as the maximizing player
            best_val = -float("inf")

            for child, divisor in self._get_children(node):
                val, _ = self.minimax_alpha_beta(child, depth - 1, alpha, beta)  # evaluates the move in the long run

                if val > best_val:
                    best_val = val
                    best_move = divisor

                alpha = max(alpha, best_val)

                if beta <= alpha:
                    break

            return best_val, best_move

        else:  # turn of the human (min player)
            best_val = float("inf")

            for child, divisor in self._get_children(node):
                val, _ = self.minimax_alpha_beta(child, depth - 1, alpha, beta)  # evaluates the move in the long run

                if val < best_val:
                    best_val = val
                    best_move = divisor

                beta = min(beta, best_val)

                if beta <= alpha:
                    break

            return best_val, best_move

    def minimax(self, node: Node, depth: int) -> tuple[int, Optional[int]]:
        """
        Runs minimax search from the given node up to a specified depth.

        This method assumes:
            - the computer is the maximizing player,
            - the human is the minimizing player.

        At each node it recursively evaluates child positions and selects the
        move (divisor) that optimizes the outcome for the current player.

        Parameters:
            node (Node): Current node to evaluate.
            depth (int): Remaining search depth. When it reaches 0, the
                         position is evaluated without further expansion.

        Returns:
            tuple[int, Optional[int]]: A pair of:
                - best_value: The minimax value of the position.
                - best_move: The divisor (move) that achieves `best_value`. Returns None
                             if the position is terminal or depth == 0.
        """
        if self.rules.is_terminal(node.state) or depth == 0:
            self.metrics.evaluated_node_count += 1
            return self.rules.evaluate(node.state), None

        best_move = None
        if node.state.turn == Player.COMPUTER:
            best_val = -float("inf")

            for child, divisor in self._get_children(node):
                val, _ = self.minimax(child, depth - 1)

                if val > best_val:
                    best_val = val
                    best_move = divisor

            return best_val, best_move

        else:  # turn of the human (min player)
            best_val = float("inf")

            for child, divisor in self._get_children(node):
                val, _ = self.minimax(child, depth - 1)  # evaluates the move in the long run

                if val < best_val:
                    best_val = val
                    best_move = divisor

            return best_val, best_move

    def change_root(self, node: Node) -> None:
        """
        Update the root of the tree.

        If the current root has no children, the root is replaced with the
        provided node.

        If the current root already has children, the method assumes that
        a node with the same state already exists among them. In this case,
        the existing child node (matching by state) is promoted to
        be the new root instead of using the provided node.

        Parameters:
            node (Node): The node intended to become the new root.

        Returns:
            None
        """
        if len(self.root.children) == 0:
            self.root = node
            return

        for child, _ in self.root.children:
            if child.state == node.state:
                self.root = child
                return

        raise ValueError("root wasn't changed")

    def _get_children(self, node: Node) -> list[tuple['Node', int]]:
        """
        Returns the child nodes of the given node.

        If the node does not yet have generated children, they are created
        using `generate_children` and returned. Otherwise, the existing
        children are returned.

        Parameters:
            node (Node): The parent node whose children are requested.

        Returns:
            list[tuple[Node, int]]: A list of (child_node, move) pairs,
                                    where `move` is the divisor used to
                                    produce the child state.
        """
        if len(node.children) == 0:
            return self._generate_children(node)
        return node.children

    # function that generates children of each state
    def _generate_children(self, node: Node) -> list[tuple['Node', int]]:
        """
        Generates and stores child nodes for all legal moves from the given node.

        For each divisor defined in the configuration, a child node is created if
        the move is legal (i.e., the current number is divisible by the divisor).
        The resulting state is computed via `GameRules.apply_move`. Generated
        children are appended to `node.children` as (child_node, divisor) pairs.

        This method mutates `node.children`.

        Parameters:
            node (Node): Node whose children should be generated.

        Returns:
            list[tuple[Node, int]]: List of (child_node, move) pairs, where `move`
                                    is the divisor used to produce the child state.
        """
        for divisor in self.rules.cfg.divisors:
            if node.state.number % divisor == 0:
                new_state = self.rules.apply_move(node.state, divisor)
                new_node = Node(new_state, [])
                self.metrics.generated_node_count += 1
                node.children.append((new_node, divisor))
        return node.children
