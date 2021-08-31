from constants import *


class BoardSpace:
    def __init__(self, action_type):
        self.action_type = action_type
        self.last_touched = 0

    def available(self, current_step):
        if self.last_touched == 0:
            return True

        if self.last_touched >= current_step:
            return True

        if current_step >= self.last_touched + 10:
            return True

        return False

    def visit(self, current_step):
        self.last_touched = current_step

    def __str__(self) -> str:
        return self.action_type
