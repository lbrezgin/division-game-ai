import sys
import os
import time

import tkinter as tk
from tkinter import ttk

from game.state import State
from game.rules import GameRules, RulesConfig
from game.tree import GameTree
from game.node import Node
from game.player import Player
from game.metrics import Metrics

class GameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Division Game")
        self.root.geometry("500x500")

        self.rules = GameRules(
            config=RulesConfig(
                lower_bound=20000,
                upper_bound=30000,
                divisors=(2, 3, 4),
                terminal_limit=10,
                max_depth=10,
                alpha_beta_optimization=True
            )
        )

        self.tree = None
        self.chosen_number = None
        self.use_alpha_beta = True
        self.game_starter = Player.HUMAN

        self.start_frame = tk.Frame(root)
        self.settings_frame = tk.Frame(root)
        self.game_frame = tk.Frame(root)
        self.start_frame.pack(fill="both", expand=True)

        self.create_start_screen()

        style = ttk.Style()
        style.theme_use("clam")   # not "calm"
        style.configure(
            "Rounded.TButton",
            padding=5,
            font=("Arial", 10)
        )

    # ------------------ START SCREEN ------------------

    def create_start_screen(self):
        tk.Label(self.start_frame, text="Choose Starting Number",
                 font=("Comic Sans", 16)).pack(pady=20)

        self.start_numbers = self.rules.start_number_generator()

        for num in self.start_numbers:
            ttk.Button(
                self.start_frame,
                text=str(num),
                width=20,
                style = "Rounded.TButton",
                command=lambda n=num: self.start_game(n)
            ).pack(pady=5)

    def start_game(self, number):
        self.chosen_number = number
        self.start_frame.pack_forget()
        self.create_settings_screen()

    # ------------------ SETTINGS SCREEN ------------------

    def create_settings_screen(self):
        self.settings_frame.pack(fill="both", expand=True)

        tk.Label(self.settings_frame, text="Game Settings",
                 font=("Comic Sans", 16)).pack(pady=20)

        # Who starts
        tk.Label(self.settings_frame, text="Who starts?",
                 font=("Arial", 12)).pack(pady=10)

        ttk.Button(
            self.settings_frame,
            text="Human Starts",
            width=20,
            style="Rounded.TButton",
            command=lambda: self.set_starter(Player.HUMAN)
        ).pack(pady=5)

        ttk.Button(
            self.settings_frame,
            text="AI Starts",
            width=20,
            style="Rounded.TButton",
            command=lambda: self.set_starter(Player.COMPUTER)
        ).pack(pady=5)

        # Algorithm
        tk.Label(self.settings_frame, text="Choose Algorithm",
                 font=("Arial", 12)).pack(pady=10)

        ttk.Button(
            self.settings_frame,
            text="Minimax",
            width=20,
            style="Rounded.TButton",
            command=lambda: self.set_algorithm(False)
        ).pack(pady=5)

        ttk.Button(
            self.settings_frame,
            text="Alpha-Beta Pruning",
            width=20,
            style="Rounded.TButton",
            command=lambda: self.set_algorithm(True)
        ).pack(pady=5)

    def set_starter(self, player):
        self.game_starter = player

    def set_algorithm(self, use_alpha_beta):
        self.use_alpha_beta = use_alpha_beta
        self.settings_frame.pack_forget()

        self.tree = GameTree(
            root=Node(
                state=State(
                    number=self.chosen_number,
                    human_points=0,
                    computer_points=0,
                    turn=self.game_starter
                ),
                children=[]
            ),
            rules=self.rules,
            metrics=Metrics(
                generated_node_count=0,
                evaluated_node_count=0,
                time_used_to_make_ai_move=0
            )
        )

        self.create_game_screen()
        self.update_ui()
        
        # If AI starts, make the first move
        if self.game_starter == Player.COMPUTER:
            self.root.after(500, self.ai_move)


    # ------------------ GAME SCREEN ------------------

    def create_game_screen(self):
        self.game_frame.pack(fill="both", expand=True)

        self.generated_node_count_label = tk.Label(self.game_frame, font=("Arial", 14))
        self.generated_node_count_label.pack()

        self.evaluated_node_count_label = tk.Label(self.game_frame, font=("Arial", 14))
        self.evaluated_node_count_label.pack()

        self.time_used_to_make_ai_move_label = tk.Label(self.game_frame, font=("Arial", 14))
        self.time_used_to_make_ai_move_label.pack()

        self.number_label = tk.Label(self.game_frame, font=("Arial", 14))
        self.number_label.pack(pady=10)

        self.human_label = tk.Label(self.game_frame, font=("Arial", 12))
        self.human_label.pack()

        self.ai_label = tk.Label(self.game_frame, font=("Arial", 12))
        self.ai_label.pack()
        
        self.ai_move_label = tk.Label(self.game_frame, font=("Arial", 12))
        self.ai_move_label.pack(pady=5)
        self.ai_move_label.config(text="AI chose: -")

        tk.Label(self.game_frame, text="Choose Divider:").pack(pady=10)
        
        self.buttons = {}
        for d in self.rules.cfg.divisors:
            
            btn = ttk.Button(
                self.game_frame,
                text=f"Divide by {d}",
                width=15,
                style = "Rounded.TButton",
                command=lambda div=d: self.human_move(div)
            )
            btn.pack(pady=3)
            self.buttons[d] = btn

        self.result_label = tk.Label(self.game_frame, font=("Arial", 16), fg="red")
        self.result_label.pack(pady=10)

        self.restart_button = ttk.Button(
            self.game_frame,
            text="Restart Game",
            width=15,  
            style = "Rounded.TButton", 
            command=self.restart_game
        )
        self.restart_button.pack(pady=10)
        self.restart_button.pack_forget()  # Hide the button until the game ends

    # ------------------ HUMAN MOVE ------------------

    def human_move(self, divisor):
        state = self.tree.root.state

        if state.number % divisor != 0:
            return

        new_state = self.rules.apply_move(state, divisor)
        self.tree.change_root(Node(new_state, []))
        self.update_ui()

        if self.rules.is_terminal(self.tree.root.state):
            self.end_game()
            return

        self.root.after(500, self.ai_move)

    # ------------------ AI MOVE ------------------

    def ai_move(self):
        start_time = time.perf_counter()

        if self.use_alpha_beta:
            _, best_move = self.tree.minimax_alpha_beta(
                self.tree.root,
                self.rules.cfg.max_depth,
                -float("inf"),
                float("inf")
            )
        else:
            _, best_move = self.tree.minimax(self.tree.root, self.rules.cfg.max_depth)

        end_time = time.perf_counter()
        self.tree.metrics.time_used_to_make_ai_move = end_time - start_time

        if best_move is None:
            self.end_game()
            return

        self.ai_move_label.config(text=f"AI chose: divide by {best_move}")
        new_state = self.rules.apply_move(self.tree.root.state, best_move)
        self.tree.change_root(Node(new_state, []))
        self.update_ui()

        if self.rules.is_terminal(self.tree.root.state):
            self.end_game()

    # ------------------ UI UPDATE ------------------

    def update_ui(self):
        state = self.tree.root.state
        self.generated_node_count_label.config(text=f"Generated nodes (whole game): {self.tree.metrics.generated_node_count}")
        self.evaluated_node_count_label.config(text=f"Evaluated nodes (whole game): {self.tree.metrics.evaluated_node_count}")
        self.time_used_to_make_ai_move_label.config(text=f"AI move time (current move): {self.tree.metrics.time_used_to_make_ai_move}")
        self.number_label.config(text=f"Current Number: {state.number}")
        self.human_label.config(text=f"Human: {state.human_points}")
        self.ai_label.config(text=f"AI: {state.computer_points}")
        if not self.ai_move_label.cget("text"):
            self.ai_move_label.config(text="AI chose: -")
        for d, btn in self.buttons.items():
            if state.number % d == 0:
                btn.config(state="normal")
            else:
                btn.config(state="disabled")

    # ------------------ GAME OVER ------------------

    def end_game(self):
        state = self.tree.root.state
        if state.human_points > state.computer_points:
            result = "Human Wins!"
        elif state.human_points < state.computer_points:
            result = "AI Wins!"
        else:
            result = "Draw!"

        self.result_label.config(text=f"Game Over!\nFinal Score - Human: {state.human_points} | AI: {state.computer_points}\n{result}")

        for btn in self.buttons.values():
            btn.config(state="disabled")

        self.restart_button.pack()

    def restart_game(self):
        os.execv(sys.executable, [sys.executable] + sys.argv)


# ------------------ RUN APP ------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = GameUI(root)
    root.mainloop()