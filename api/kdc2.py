memo = {}


class BoardSpaceType:
    FLOWER_GARDEN = "Flower Garden"


class Direction:
    LEFT = "Left"
    RIGHT = "Right"
    UP = "Up"
    DOWN = "Down"


def recurse(direction, road, route, state, step=0, visited=None):

    if (direction, road) in memo:
        memoized_state = memo[(direction, road)]

        if (state + memoized_state):
            pass
        else:
            pass

    for action in road.actions(direction):
        if action in BoardSpaceType:
            # Skip Flower Garden if route already contains it
            if action == BoardSpaceType.FLOWER_GARDEN and \
                    BoardSpaceType.FLOWER_GARDEN in route:
                continue

            if action not in visited:
                visited[action] = step
            elif step - visited[action] > 10:
                visited[action] = step
            else:
                continue

        route.add(action)

        if action in Direction:
            pass

        if action in visited:
            continue


# NOTES
# A value state coming into the road/direction may not play well with the value state saved
# 
# When memoizing, we need to memo the visited dictionary as well