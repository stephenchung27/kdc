from kdc import KarutaDateCalculator
from constants import Direction


blank_board = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None],
        [None, None, None, None, None]
    ]
}


def joes_board():
    return {
        "horizontal_roads": [
            [True, True, True, True, True],
            [True, False, True, True, True],
            [False, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [False, True, True, False, True],
            [False, False, True, True, True],
            [True, True, True, True, True],
        ],
        "vertical_roads": [
            [True, True, True, True, False, True],
            [True, True, True, True, False, True],
            [True, True, False, True, True, True],
            [True, False, True, True, False, True],
            [True, True, False, True, True, True],
            [True, True, True, True, True, True],
            [True, True, True, True, True, True],
        ],
        "board_spaces": [
            ["Fair", None, "Nightclub", "Juice", "Jewelry Store"],
            ["Sandwich Shop", None, "Gas Station", None, None],
            ["Gas Station", "Italian", None, None, "Shopping Mall"],
            [None, None, None, "Coffee", None],
            ["Taco", "Home", None, "Gas Station", None],
            [None, None, "Theatre", None, "Flower Garden"],
            ["Ballroom", "Airport", None, None, None]
        ]
    }


def stephens_board():
    return {
        "horizontal_roads": [
            [True, True, True, True, True],
            [True, False, True, True, True],
            [False, False, True, False, True],
            [True, True, True, False, True],
            [True, True, True, False, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
        ],
        "vertical_roads": [
            [True, True, True, True, True, True],
            [True, True, True, True, True, True],
            [True, True, True, True, True, True],
            [True, False, True, True, True, True],
            [True, True, False, True, True, True],
            [True, True, False, True, False, True],
            [True, True, True, True, True, True],
        ],
        "board_spaces": [
            ["Gas Station", None, None, None, None],
            [None, None, "Flower Garden", None, None],
            [None, None, None, "Italian", "Fair"],
            [None, None, "Home", "Juice", "Ballroom"],
            ["Nightclub", "Gas Station", "Sandwich Shop", None, None],
            ["Airport", "Taco", "Theatre", None, None],
            [None, "Gas Station", None, None, "Coffee"]
        ]
    }


def joe_second_board():
    return {
        "horizontal_roads": [
            [True, True, True, True, True],
            [False, True, True, True, True],
            [False, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
            [False, True, True, True, True],
            [True, True, True, True, True],
            [True, True, True, True, True],
        ],
        "vertical_roads": [
            [True, True, True, True, True, True],
            [True, True, False, False, True, True],
            [True, True, False, True, False, True],
            [True, False, False, False, True, True],
            [True, True, True, True, False, True],
            [True, True, False, True, True, True],
            [True, True, True, True, True, True],
        ],
        "board_spaces": [
            ["Italian", None, None, None, "Nightclub"],
            ["Gas Station", None, "Airport", "Juice", None],
            [None, None, None, None, None],
            [None, None, None, "Ballroom", "Theatre"],
            ["Fair", None, None, None, "Coffee"],
            ["Home", "Taco", "Sandwich Shop", None, None],
            ["Gas Station", None, "Flower Garden", "Gas Station", None]
        ]
    }


stephen_2 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True],
        [False, True, True, True, True],
        [False, True, False, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, False, False, True, True],
        [True, True, False, False, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, False, True],
        [True, True, True, False, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, None, None, "Gas Station"],
        ["Gas Station", "Home", None, "Theatre", None],
        [None, "Coffee", None, "Flower Garden", "Sandwich Shop"],
        [None, "Taco", "Fair", "Juice", None],
        [None, "Shopping Mall", None, "Nightclub", None],
        [None, None, None, "Gas Station", "Airport"],
        [None, "Ballroom", None, None, "Italian"]
    ],
    "direction": Direction.R
}

stephen_3 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, False, True, False, True],
        [True, False, True, False, True],
        [True, True, False, False, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, False, True, False, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, None, "Flower Garden", "Sandwich Shop"],
        ["Coffee", "Airport", None, None, "Ballroom"],
        ["Theatre", None, "Gas Station", "Italian", None],
        [None, None, None, None, None],
        ["Fair", None, None, None, "Juice"],
        [None, "Gas Station", "Gas Station", None, None],
        [None, None, "Nightclub", "Home", "Taco"]
    ],
    "direction": Direction.R
}

board = stephen_3

kdc = KarutaDateCalculator()
kdc(board, board["direction"])

print(f"""
Best Successful Route
{kdc.best_successful_route}
{kdc.best_successful_route.value_state if kdc.best_successful_route else ""}

Shopping
{kdc.best_route_with_shopping}
{kdc.best_route_with_shopping.value_state if kdc.best_route_with_shopping else ""}

Shopping + Ring
{kdc.best_route_with_shopping_and_ring}
{kdc.best_route_with_shopping_and_ring.value_state if kdc.best_route_with_shopping_and_ring else ""}

Shopping + Home
{kdc.best_route_with_shopping_and_home}
{kdc.best_route_with_shopping_and_home.value_state if kdc.best_route_with_shopping_and_home else ""}

Jewelry Store
{kdc.best_route_with_jewelry_store}
{kdc.best_route_with_jewelry_store.value_state if kdc.best_route_with_jewelry_store else ""}

Home
{kdc.best_route_with_home}
{kdc.best_route_with_home.value_state if kdc.best_route_with_home else ""}

Airport
{kdc.best_route_with_airport}
{kdc.best_route_with_airport.value_state if kdc.best_route_with_airport else ""}
""")
