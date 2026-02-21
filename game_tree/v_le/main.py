import random

from game_tree import GameTree
from state import State
from node import Node


def generate_random(a: int, b: int) -> int:
    """
    Return random integer in range [a, b], inclusive,
    divisible by 2, 3, and 4.
    """
    valid = [x for x in range(a, b + 1) if x % 12 == 0]
    return random.choice(valid)

RANGE_A = 20000
RANGE_B = 30000
GAME_STATUS = True
start = {1: "HUMAN", 2: "AI"}

rand_numbers = []
for _ in range(5):
    rand_numbers.append(generate_random(RANGE_A, RANGE_B))

# initial_state = State(number=36)
# root = Node(parent=None, state=initial_state)
# tree = GameTree(root)
# print(tree.minimax(current_node=root, depth=100, maximizing_player=True))

while GAME_STATUS:
    print("Choose the number to play with!")
    choose = ""
    for i in range(len(rand_numbers)):
        choose += f"{i+1} — {rand_numbers[i]}\n"

    print(choose)
    chosen_digit = input()
    chosen_number = rand_numbers[int(chosen_digit)-1]
    print(f"You have chosen {chosen_number}.")
    print("Who starts the game?\n1 — You\n2 — AI ")
    starts = input()
    print(f"Nice! {start[int(starts)]}")
