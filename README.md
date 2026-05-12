# Division Game AI
A Python GUI strategy game built with Tkinter featuring an AI opponent powered by the [Minimax](https://en.wikipedia.org/wiki/Minimax#:~:text=A%20minimax%20algorithm%20is%20a,or%20state%20of%20the%20game.) Algorithm and [Alpha–beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) Pruning algorithms. The project demonstrates adversarial search, recursive game tree generation, and AI decision-making in a competitive mathematical game.

## Game Rules
At the start of the game, the program randomly generates `5` numbers in the range from `200000` to `500000`. Only numbers divisible by `2`, `3`, and `4` are generated. The player selects one of the generated numbers to begin the game.

### Gameplay
* Both players start with `0` points
* Players take turns
* On each turn, the current number can be divided by:
   * `2`
   * `3`
   * `4`
* Division is allowed only if the result is an integer

### Scoring
After division:
* If the resulting number is even `->` the opponent loses 1 point
* If the resulting number is odd `->` the current player gains 1 point

### End Condition
The game ends when the current number becomes less than or equal to 10.

### Winner
* Equal points `->` draw
* More points `->` winner

## Features
* Graphical user interface built with Tkinter
* Human vs AI gameplay
* Minimax algorithm implementation
* Alpha-Beta pruning optimization
* Recursive game tree search
* Turn-based strategy mechanics

## Technologies
* Python
* Tkinter
* Object-oriented programming
* Recursive algorithms
* Tree data structures
* Adversarial search

## AI Algorithms
### Minimax
The AI evaluates future game states and chooses moves that maximize its advantage while minimizing the opponent’s best possible outcome.

### Alpha-Beta Pruning
Alpha-Beta pruning optimizes Minimax by removing branches that cannot influence the final decision, significantly improving performance.

## How to Run

```
python main.py
```
