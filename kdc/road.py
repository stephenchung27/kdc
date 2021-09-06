from collections import defaultdict
from action import Action


class Road():
    def __init__(self):
        self.board_space_actions = []
        self.road_actions = defaultdict(list)

    def __getitem__(self, key):
        return self.road_actions[key]

    def add_board_space_action(self, board_space, board_space_type):
        board_space_action = Action(board_space, board_space_type)
        self.board_space_actions.append(board_space_action)

    def add_road_action(self, road, facing_direction, going_direction):
        road_action = Action(road, going_direction)
        self.road_actions[facing_direction].append(road_action)

    def available_road_actions(self, direction):
        return self.road_actions[direction]

    def block(self):
        for direction in self.road_actions:
            for road_action in self.road_actions[direction]:
                road_action.action.remove_road(self)

    def remove_road(self, road):
        for direction in self.road_actions:
            for road_action in self.road_actions[direction]:
                if road_action.action is road:
                    self.road_actions[direction].remove(road_action)

    def available_actions(self, direction):
        return self.board_space_actions + \
            self.available_road_actions(direction)
