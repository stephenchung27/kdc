from .constants import *


class BoardSpace:
    def __init__(self, action_type):
        self.action_type = action_type

    def __str__(self) -> str:
        return self.action_type.value

    def __hash__(self):
        return hash(repr(self))
