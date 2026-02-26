from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Tuple

def start_number_generator(count: int = 5, lo: int = 20000, hi: int = 30000) -> List[int]:
    numbers = set()

    while len(numbers) < count:
        n = random.randint(lo, hi)

        if n % 12 == 0: # divisible by 2,3,4
            numbers.add(n)

    return sorted(numbers)

@dataclass(frozen=True)
class State:
    number: int
    human_points: int
    computer_points: int
    turn: str

# function that generates children of each state
def generate_children(state: State):
    children: List[Tuple[State, int]] = []

    for divisor in [2, 3, 4]:
        if state.number % divisor == 0:
            new_number = state.number // divisor

            human_points = state.human_points
            computer_points = state.computer_points

            if state.turn == "human":
                human_points += 1
                next_turn = "computer"
                
            else:
                computer_points += 1
                next_turn = "human"

            new_state = State(new_number, human_points, computer_points, next_turn)
            children.append((new_state, divisor))
            
    return children

def is_terminal(state: State) -> bool:
    if state.number <= 10:
        return True
    
    for d in (2, 3, 4):
        if state.number % d == 0:
            return False
        
    return True



def evaluate(state: State):
    return state.computer_points - state.human_points

def minimax(state: State, alpha: float, beta: float):
    if is_terminal(state):
        return evaluate(state), None
    
    if state.turn == "computer": # computer is chosen as the maximizing player
        best_move = None
        best_val = -float("inf")
        
        for child, divisor in generate_children(state):
           val, _ = minimax(child, alpha, beta) # evaluates the move in the long run

           if val > best_val:
              best_val = val
              best_move = divisor

           alpha = max(alpha, best_val)

           if beta <= alpha:
               break
        
        return best_val, best_move

    else: # turn of the human (min player)
        best_move = None
        best_val = float("inf")

        for child, divisor in generate_children(state):
           val, _ = minimax(child, alpha, beta) # evaluates the move in the long run 

           if val < best_val:
                best_val = val
                best_move = divisor 

           beta = min(beta, best_val)

           if beta <= alpha:
               break

        return best_val, best_move

def apply_move(state: State, divisor: int) -> State:
    new_number = state.number // divisor

    even = (new_number % 2 == 0)

    human_points = state.human_points
    computer_points = state.computer_points

    if state.turn == "human":
        if even:
            computer_points -= 1
        else:
            human_points += 1
        next_turn = "computer"

    else:
        if even:
            human_points -= 1
        else:
            computer_points += 1
        next_turn = "human"

    return State(new_number, human_points, computer_points, next_turn)

def main():
    numbers = start_number_generator()
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
    state = State(chosen_number, 0, 0, "human")

    while not is_terminal(state):
        print(f"Current number: {state.number}")
        print(f"SCORE: H {state.human_points}, C {state.computer_points}\n")

        if state.turn == "human":
            while True:
                try:
                    divisor = int(input("Divide by (2/3/4): "))
                except ValueError:
                    print("Please enter an integer.")
                    continue

                if divisor not in (2, 3, 4):
                    print("Illegal divisor.")
                    continue
                if state.number % divisor != 0:
                    print("The number is not divisible by the chosen divisor.")
                    continue
                break

            state = apply_move(state, divisor)

        else:
            best_val, best_move = minimax(state, -float("inf"), float("inf"))

            state = apply_move(state, best_move)

            print("\033[92m", end="")  # start green

            print(f"Current number: {state.number}")
            print(f"SCORE: H {state.human_points}, C {state.computer_points}")
            print(f"Divide by: {best_move}\n")

            print("\033[0m", end="")  # reset color

    print("---GAME OVER---")
    print(f"Final Score: H {state.human_points}, C {state.computer_points}")

    if state.human_points > state.computer_points:
        print("Winner: Human")
    elif state.human_points < state.computer_points:
        print("Winner: Computer")
    else:
        print("Draw")

if __name__=="__main__":
    main()
