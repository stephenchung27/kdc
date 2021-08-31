from karuta_date_calculator import KarutaDateCalculator
from constants import Direction


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


kdc = KarutaDateCalculator()
kdc(joes_board(), Direction.L)

print(kdc.best_successful_route)
print(kdc.best_route_with_shopping_and_ring)
print(kdc.best_route_with_shopping)
print(kdc.best_route_with_jewelry_store)
print(kdc.best_route_with_home)
print(kdc.best_route_with_airport)
