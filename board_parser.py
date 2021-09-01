from constants import Direction, BoardSpaceType
from road import Road
from board_space import BoardSpace


class BoardParser:
    def __init__(self, json_board):
        self.board = json_board
        self.horizontal_roads = [
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road()]
        ]
        self.vertical_roads = [
            [Road(), Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road(), Road()],
            [Road(), Road(), Road(), Road(), Road(), Road()]
        ]
        self.setup_roads()
        self.parse_blocked_roads()
        self.parse_board_spaces()

    def setup_roads(self):
        for y, row in enumerate(self.horizontal_roads):
            for x, road in enumerate(row):
                if x - 1 >= 0:
                    road.add_road_action(
                        self.horizontal_roads[y][x-1],
                        Direction.L, Direction.L)
                if x + 1 < len(row):
                    road.add_road_action(
                        self.horizontal_roads[y][x+1],
                        Direction.R, Direction.R)
                if y - 1 >= 0:
                    road.add_road_action(
                        self.vertical_roads[y-1][x],
                        Direction.L, Direction.U)
                    road.add_road_action(
                        self.vertical_roads[y-1][x+1],
                        Direction.R, Direction.U)
                if y + 1 < len(self.horizontal_roads):
                    road.add_road_action(
                        self.vertical_roads[y][x],
                        Direction.L, Direction.D)
                    road.add_road_action(
                        self.vertical_roads[y][x+1],
                        Direction.R, Direction.D)

        for y, row in enumerate(self.vertical_roads):
            for x, road in enumerate(row):
                if y - 1 >= 0:
                    road.add_road_action(
                        self.vertical_roads[y-1][x],
                        Direction.U, Direction.U)
                if y + 1 < len(self.vertical_roads):
                    road.add_road_action(
                        self.vertical_roads[y+1][x],
                        Direction.D, Direction.D)
                if x - 1 >= 0:
                    road.add_road_action(
                        self.horizontal_roads[y][x-1],
                        Direction.U, Direction.L)
                    road.add_road_action(
                        self.horizontal_roads[y+1][x-1],
                        Direction.D, Direction.L)
                if x + 1 < len(row):
                    road.add_road_action(
                        self.horizontal_roads[y][x],
                        Direction.U, Direction.R)
                    road.add_road_action(
                        self.horizontal_roads[y+1][x],
                        Direction.D, Direction.R)

    def parse_blocked_roads(self):
        for y, row in enumerate(self.board["horizontal_roads"]):
            for x, road_unblocked in enumerate(row):
                if not road_unblocked:
                    self.horizontal_roads[y][x].block()

        for y, row in enumerate(self.board["vertical_roads"]):
            for x, road_unblocked in enumerate(row):
                if not road_unblocked:
                    self.vertical_roads[y][x].block()

    def parse_board_spaces(self):
        for y, row in enumerate(self.board["board_spaces"]):
            for x, board_space_type in enumerate(row):
                if board_space_type is None:
                    continue

                board_space_type = BoardSpaceType(board_space_type)
                board_space = BoardSpace(board_space_type)

                self.horizontal_roads[y][x].add_board_space_action(
                    board_space, board_space_type)
                self.horizontal_roads[y+1][x].add_board_space_action(
                    board_space, board_space_type)
                self.vertical_roads[y][x].add_board_space_action(
                    board_space, board_space_type)
                self.vertical_roads[y][x+1].add_board_space_action(
                    board_space, board_space_type)
