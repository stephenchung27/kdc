from pytest import fixture
from board_parser import BoardParser


@fixture
def blank_json_board():
    return {
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


@fixture
def board_spaces():
    return [
        ["Fair", None, "Nightclub", "Juice Bar", "Jewelry Store"],
        ["Sandwich Shop", None, "Gas Station", None, None],
        ["Gas Station", "Italian Restaurant", None, None, "Shopping Mall"],
        [None, None, None, "Coffee", None],
        ["Taco Stand", "Home", None, "Gas Station", None],
        [None, None, "Theatre", None, "Flower Garden"],
        ["Ballroom", "Airport", None, None, None]
    ]


@fixture
def filled_json_board(board_spaces):
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
        "board_spaces": board_spaces
    }
