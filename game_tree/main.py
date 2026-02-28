from __future__ import annotations

from tree import GameTree
from rules import GameRules, RulesConfig
from state import State
from node import Node
from player import Player

def main():
    game_rules = GameRules(
        config=RulesConfig(
            lower_bound=20000,
            upper_bound=30000,
            divisors=(2, 3, 4),
            terminal_limit=10,
            max_depth=10,
            alfa_beta_optimization=True
        )
    )

    numbers = game_rules.start_number_generator()
    print("Choose a number by typing its index to start the game:")
    
    for i, n in enumerate(numbers, start=1):
        print(f"[{i}] {n}")

    while True:
        try:
            chosen_index = int(input(""))
            if 1 <= chosen_index <= 5:
                break
            print("Invalid choice")
        except ValueError:
            print("Enter a number.")

    chosen_number = numbers[chosen_index - 1]

    # Tree is the primary interface for interacting with the game logic.
    # All state modifications must be performed through the `tree` instance.
    #
    # Through `tree`, you have access to:
    # - the current game state via the root node (`root`)
    # - the rule set (`rules`)
    # - all required methods for move
    tree = GameTree(
        root=Node(
            state=State(
                number=chosen_number,
                human_points=0,
                computer_points=0,
                turn=Player.HUMAN
            ),
            children=[]
        ),
        rules=game_rules
    )

    while not tree.rules.is_terminal(tree.root.state):
        print(f"Current number: {tree.root.state.number}")
        print(f"SCORE: H {tree.root.state.human_points}, C {tree.root.state.computer_points}\n")

        if tree.root.state.turn == Player.HUMAN:
            while True:
                try:
                    divisor = int(input("Divide by (2/3/4): "))
                except ValueError:
                    print("Please enter an integer.")
                    continue

                if divisor not in tree.rules.cfg.divisors:
                    print("Illegal divisor.")
                    continue
                if tree.root.state.number % divisor != 0:
                    print("The number is not divisible by the chosen divisor.")
                    continue
                break

            state = tree.rules.apply_move(tree.root.state, divisor)
            tree.change_root(Node(state, []))

        else:
            if tree.rules.cfg.alfa_beta_optimization:
                best_val, best_move = tree.minimax_alfa_beta(
                    tree.root,
                    tree.rules.cfg.max_depth,
                    -float("inf"),
                    float("inf")
                )
            else:
                best_val, best_move = tree.minimax(tree.root, tree.rules.cfg.max_depth)

            state = tree.rules.apply_move(tree.root.state, best_move)
            tree.change_root(Node(state, []))

            print("\033[92m", end="")  # start green

            print(f"Current number: {tree.root.state.number}")
            print(f"SCORE: H {tree.root.state.human_points}, C {tree.root.state.computer_points}")
            print(f"Divide by: {best_move}\n")

            print("\033[0m", end="")  # reset color

    print("---GAME OVER---")
    print(f"Final Score: H {tree.root.state.human_points}, C {tree.root.state.computer_points}")

    if tree.root.state.human_points > tree.root.state.computer_points:
        print("Winner: Human")
    elif tree.root.state.human_points < tree.root.state.computer_points:
        print("Winner: Computer")
    else:
        print("Draw")

if __name__=="__main__":
    main()
