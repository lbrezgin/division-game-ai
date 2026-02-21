from dataclasses import dataclass

@dataclass
class State:
    number: int
    human_points: int = 0
    ai_points: int = 0