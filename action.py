from constants import Direction, BoardSpaceType


class Action:
    def __init__(self, action, action_type=None):
        self.action = action
        if action_type is None and isinstance(action.action_type, BoardSpaceType):
            self.action_type = action.action_type
        else:
            self.action_type = action_type
        self.determine_values(self.action_type)

    def determine_values(self, action_type):
        if action_type == BoardSpaceType.G:
            self.set_values(fuel=100)
        elif action_type == BoardSpaceType.P:
            self.set_values(food=56)
        elif action_type == BoardSpaceType.T:
            self.set_values(food=56)
        elif action_type == BoardSpaceType.S:
            self.set_values(food=36, drink=14)
        elif action_type == BoardSpaceType.F:
            self.set_values(food=16, drink=14, entertainment=32)
        elif action_type == BoardSpaceType.J:
            self.set_values(drink=54)
        elif action_type == BoardSpaceType.C:
            self.set_values(drink=54)
        elif action_type == BoardSpaceType.N:
            self.set_values(drink=34, entertainment=32)
        elif action_type == BoardSpaceType.L:
            self.set_values(entertainment=92)
        elif action_type == BoardSpaceType.B:
            self.set_values(entertainment=92)
        elif action_type == BoardSpaceType.R:
            self.set_values(entertainment=52)
        elif action_type == BoardSpaceType.A:
            self.set_values(entertainment=-18)
        elif action_type == BoardSpaceType.E:
            self.set_values()
        elif action_type == BoardSpaceType.M:
            self.set_values()
        elif action_type == BoardSpaceType.H:
            self.set_values()
        elif isinstance(action_type, Direction):
            self.set_values()

    def set_values(self, fuel=-10, food=-4, drink=-6, entertainment=-8):
        self.fuel = fuel
        self.food = food
        self.drink = drink
        self.entertainment = entertainment

    def __str__(self):
        return self.action_type.value
