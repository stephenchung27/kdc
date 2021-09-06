from value_state import ValueState
from constants import BoardSpaceType


class Route:
    def __init__(self):
        self.value_state = ValueState()
        self.route = []

    def __eq__(self, other):
        return self.value_state == other.value_state

    def __lt__(self, other):
        return self.value_state < other.value_state

    def __getitem__(self, key):
        return self.route[key]

    def __str__(self):
        return ", ".join([str(action) for action in self.route])

    def to_array(self):
        return [str(action) for action in self.route]

    def __len__(self):
        return len(self.route)

    @property
    def total_value(self):
        return self.value_state.total_value

    @property
    def successful(self):
        return self.valid and self.value_state.time == 0

    @property
    def valid(self):
        return self.value_state.valid

    @property
    def took_home(self):
        return self.contains(BoardSpaceType.H)

    @property
    def took_airport(self):
        return self.contains(BoardSpaceType.A)

    def contains(self, action_type):
        for action in self.route:
            if action.action_type == action_type:
                return True
        return False

    def add_action(self, action):
        self.route.append(action)
        self.value_state.calculate_action(action)

    def copy(self):
        new_route = Route()
        new_route.value_state = ValueState(
            fuel=self.value_state.fuel,
            food=self.value_state.food,
            drink=self.value_state.drink,
            entertainment=self.value_state.entertainment,
            time=self.value_state.time,
        )
        new_route.route = list(self.route)
        return new_route
