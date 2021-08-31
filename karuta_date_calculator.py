from board_parser import BoardParser
from constants import Direction, BoardSpaceType
from route import Route


class KarutaDateCalculator:
    def __init__(self):
        self.possible_routes = []

    @property
    def best_successful_route(self):
        successful_routes = [
            route
            for route in self.possible_routes
            if route.successful
        ]

        if successful_routes:
            return max(successful_routes)
        else:
            return None

    @property
    def best_route_with_shopping_and_ring(self):
        successful_routes = [
            route
            for route in self.possible_routes
            if route.successful and
            route.contains(BoardSpaceType.M) and
            route.contains(BoardSpaceType.E)
        ]

        non_successful_routes = [
            route
            for route in self.possible_routes
            if route.contains(BoardSpaceType.M) and
            route.contains(BoardSpaceType.E)
        ]

        if successful_routes:
            return max(successful_routes)
        elif non_successful_routes:
            return min(non_successful_routes, key=len)
        else:
            return None

    @property
    def best_route_with_shopping(self):
        successful_routes = [
            route
            for route in self.possible_routes
            if route.successful and
            route.contains(BoardSpaceType.M)
        ]

        non_successful_routes = [
            route
            for route in self.possible_routes
            if route.contains(BoardSpaceType.M)
        ]

        if successful_routes:
            return max(successful_routes)
        elif non_successful_routes:
            return min(non_successful_routes, key=len)
        else:
            return None

    @property
    def best_route_with_jewelry_store(self):
        successful_routes = [
            route
            for route in self.possible_routes
            if route.successful and
            route.contains(BoardSpaceType.E)
        ]

        non_successful_routes = [
            route
            for route in self.possible_routes
            if route.contains(BoardSpaceType.E)
        ]

        if successful_routes:
            return max(successful_routes)
        elif non_successful_routes:
            return min(non_successful_routes, key=len)
        else:
            return None

    @property
    def best_route_with_home(self):
        home_routes = [
            route
            for route in self.possible_routes
            if route.took_home
        ]

        if home_routes:
            return max(home_routes, key=len)
        else:
            return None

    @property
    def best_route_with_airport(self):
        airport_routes = [
            route
            for route in self.possible_routes
            if route.took_airport
        ]

        if airport_routes:
            return max(airport_routes or [])
        else:
            return None

    def calculate_all_possible_routes(self):
        def recurse(direction, current_road, route, step=1):
            if route.valid and route.successful:
                self.possible_routes.append(route)
                return

            if not route.valid:
                if route.contains(BoardSpaceType.M) or \
                        route.contains(BoardSpaceType.E):
                    self.possible_routes.append(route)
                return

            for action in current_road.available_actions(direction, step):
                new_route = route.copy()

                if isinstance(action.action_type, BoardSpaceType):
                    action.action.visit(step)

                new_route.add_action(action)

                if isinstance(action.action_type, Direction):
                    recurse(action.action_type, action.action, new_route, step + 1)

                elif isinstance(action.action_type, BoardSpaceType) and \
                        action.action.available(step):
                    if action.action_type in (BoardSpaceType.H, BoardSpaceType.A):
                        self.possible_routes.append(new_route)
                        continue

                    recurse(direction, current_road, new_route, step + 1)

        recurse(self.initial_direction, self.initial_road, Route())

    def __call__(self, json_board, initial_direction):
        board_parser = BoardParser(json_board)
        self.initial_road = board_parser.horizontal_roads[-1][2]
        self.initial_direction = initial_direction

        self.calculate_all_possible_routes()
