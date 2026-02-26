from dataclasses import dataclass
from typing import Optional

from state import State


@dataclass
class Node:
    parent: Optional['Node']
    state: State
