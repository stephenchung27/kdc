from board_parser import BoardParser
from constants import Direction, BoardSpaceType
from route import Route


class KarutaDateCalculator:
    def __init__(self):
        self.possible_routes = []

    def calculate_all_possible_routes(self):
        def recurse(direction, current_road, route, step=0, visited=None):
            if visited is None:
                visited = dict()

            if route.successful:
                self.possible_routes.append(route)
                return

            # Add to possible_routes if Shopping Mall or Jewelry Store
            if not route.valid:
                if route.contains(BoardSpaceType.M) or \
                        route.contains(BoardSpaceType.E):
                    self.possible_routes.append(route)
                return

            for action in current_road.available_actions(direction):
                new_route = route.copy()
                new_visited = visited.copy()

                if action.action_type in BoardSpaceType:
                    if action.action not in new_visited:
                        new_visited[action.action] = step
                    elif step - new_visited[action.action] > 10:
                        new_visited[action.action] = step
                    else:
                        continue

                # Action has been added to new_route after this point
                new_route.add_action(action)

                if action.action_type in Direction:
                    recurse(action.action_type, action.action, new_route,
                            step + 1, new_visited)
                elif action.action_type in BoardSpaceType:
                    # Add to possible_routes if Home or Airport
                    if action.action_type in (BoardSpaceType.H,
                                              BoardSpaceType.A):
                        self.possible_routes.append(new_route)
                        continue

                    recurse(direction, current_road, new_route, step + 1,
                            new_visited)

        recurse(self.initial_direction, self.initial_road, Route())

    def __call__(self, json_board, initial_direction):
        board_parser = BoardParser(json_board)
        self.initial_road = board_parser.horizontal_roads[-1][2]
        self.initial_direction = initial_direction
        self.calculate_all_possible_routes()

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
    def best_route_with_shopping_and_home(self):
        non_successful_routes = [
            route
            for route in self.possible_routes
            if route.contains(BoardSpaceType.M) and
            route.contains(BoardSpaceType.H)
        ]

        if non_successful_routes:
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
