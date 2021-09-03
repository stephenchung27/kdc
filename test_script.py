from kdc import KarutaDateCalculator
from constants import Direction


Gas = "Gas Station"
Italian = "Italian"           # P for sPaghetti
Taco = "Taco"
Sandwich = "Sandwich Shop"
Fair = "Fair"
Juice = "Juice"
Coffee = "Coffee"
Nightclub = "Nightclub"
Flower = "Flower Garden"     # L for fLower garden
Ballroom = "Ballroom"
Theatre = "Theatre"           # R for theatRe
Airport = "Airport"
Ring = "Jewelry Store"     # E for jEwelry store
Mall = "Shopping Mall"     # M for Mall
Home = "Home"

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
    ],
    "direction": None
}

joe_1 = {
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
    ],
    "direction": Direction.L 
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

# Jewelry Store with Success
stephen_4 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, False, True, True],
        [True, False, True, False, True],
        [True, True, True, False, True],
        [True, True, True, False, True],
        [False, False, False, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, False, False, True],
        [True, False, True, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        ["Home", None, None, "Italian", "Juice"],
        [None, "Theatre", "Coffee", None, None],
        ["Jewelry Store", "Taco", "Gas Station", "Flower Garden", "Nightclub"],
        [None, None, None, None, None],
        [None, "Gas Station", None, None, None],
        ["Gas Station", None, "Ballroom", "Airport", None],
        ["Fair", None, None, None, "Sandwich Shop"]
    ],
    "direction": Direction.L
}

stephen_5 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, False, True, True, True],
        [False, True, False, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, False, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, False, False, True, False, True],
        [True, True, False, False, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, None, None, "Home"],
        [None, None, None, "Gas Station", "Italian"],
        [None, None, "Gas Station", None, None],
        ["Gas Station", None, None, "Taco", "Ballroom"],
        ["Nightclub", "Jewelry Store", "Flower Garden", "Coffee", None],
        ["Theatre", "Juice", None, "Fair", "Sandwich Shop"],
        [None, None, None, None, "Airport"]
    ],
    "direction": Direction.L
}

joe_2 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, False, False, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, False, True, True, True],
        [True, False, False, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, False, False, True, True],
        [True, False, True, True, True, True],
        [True, False, True, True, True, True],
        [True, True, False, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        ["Nightclub", "Theatre", None, "Juice", None],
        [None, "Gas Station", None, None, None],
        ["Home", None, None, "Sandwich Shop", "Taco"],
        ["Fair", None, None, None, "Airport"],
        ["Coffee", "Gas Station", None, None, None],
        [None, None, "Italian", None, "Flower Garden"],
        [None, "Ballroom", "Gas Station", None, "Shopping Mall"]
    ],
    "direction": Direction.R
}

eric_1 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [False, True, True, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, False, True, True, True, True],
        [True, False, True, False, False, True],
        [True, True, True, True, True, True],
        [True, True, True, False, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, "Flower Garden", "Nightclub", "Airport"],
        ["Juice", None, None, "Gas Station", "Sandwich Shop"],
        [None, "Theatre", None, None, None],
        ["Gas Station", None, None, None, None],
        ["Taco", "Fair", "Ballroom", None, None],
        ["Coffee", None, None, None, None],
        [None, "Home", "Gas Station", "Italian", None]
    ],
    "direction": Direction.L
}

ryan_1 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, False, False, True, True, True],
        [True, True, True, True, False, True],
        [True, True, False, True, True, True],
        [True, False, True, True, False, True],
        [True, True, False, True, True, True],
        [True, True, True, False, False, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, "Airport", None, None, None],
        [None, None, "Italian", "Taco", None],
        ["Nightclub", "Fair", "Flower Garden", "Sandwich Shop", None],
        [None, "Juice", "Theatre", None, "Coffee"],
        [None, None, None, None, "Ballroom"],
        [None, None, "Gas Station", "Gas Station", None],
        [None, None, None, "Home", "Gas Station"]
    ],
    "direction": Direction.R
}

pony_1 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, True, True, True, True],
        [True, False, True, True, True],
        [True, True, True, False, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, False, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, False, True, True, True, True],
        [True, False, True, True, False, True],
        [True, True, False, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        ["Taco", "Theatre", None, None, "Gas Station"],
        [None, None, "Fair", None, None],
        [None, None, "Gas Station", None, None],
        ["Airport", "Italian", None, None, "Flower Garden"],
        [None, None, None, None, None],
        ["Juice", "Home", "Gas Station", "Ballroom", None],
        ["Nightclub", "Sandwich Shop", None, "Coffee", None]
    ],
    "direction": Direction.L
}

ryan_2 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, False, True, True, True, True],
        [True, False, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, False, True, True, True],
        [True, False, True, True, True, True],
        [True, False, True, True, False, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        ["Gas Station", None, None, "Italian", None],
        [None, None, "Home", "Flower Garden", "Theatre"],
        [None, "Gas Station", None, "Nightclub", None],
        ["Juice", None, "Sandwich Shop", "Gas Station", None],
        [None, None, None, None, None],
        [None, "Taco", None, None, None],
        ["Coffee", "Airport", "Fair", None, "Ballroom"]
    ],
    "direction": Direction.R
}

stephen_6 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, False, True, True, True],
        [False, False, False, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, False, True, True, False, True],
        [True, False, False, True, False, True],
        [True, True, True, False, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, False, True, True, False, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, None, "Nightclub", None],
        [None, "Coffee", "Juice", None, "Sandwich Shop"],
        ["Taco", None, None, None, None],
        ["Shopping Mall", "Gas Station", "Italian", "Gas Station", "Airport"],
        ["Theatre", None, None, None, "Home"],
        [None, None, None, "Ballroom", "Flower Garden"],
        [None, "Gas Station", "Fair", None, None]
    ],
    "direction": Direction.R
}

eric_2 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, False, False, True, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, False, False, True, True],
        [True, False, False, True, True, True],
        [True, True, True, True, True, True],
        [True, True, False, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        ["Airport", "Taco", None, None, None],
        ["Gas Station", None, None, "Ballroom", None],
        ["Theatre", None, None, None, "Home"],
        [None, None, None, None, "Gas Station"],
        ["Gas Station", "Sandwich Shop", None, None, "Italian"],
        ["Nightclub", None, None, None, None],
        ["Juice", "Fair", "Flower Garden", None, "Coffee"]
    ],
    "direction": Direction.L
}

stephen_7 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, True, False, True],
        [True, True, False, False, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [False, False, True, False, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, False, True, True, True, True],
        [True, True, True, True, True, True],
        [True, False, True, True, True, True],
        [True, False, False, False, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [Theatre, Juice, Sandwich, None, None],
        [None, None, None, Gas, Taco],
        [Airport, None, None, None, None],
        [None, Flower, None, Gas, None],
        [None, Fair, None, None, None],
        [Coffee, None, Ballroom, None, Nightclub],
        [Gas, None, None, Home, Italian]
    ],
    "direction": Direction.L
}

joe_3 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [True, False, False, True, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, False, True, True, True, True],
        [True, False, True, True, False, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, False, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, None, None, None],
        [None, Sandwich, Gas, Airport, Juice],
        [None, Ballroom, Gas, Fair, None],
        [None, Flower, None, Coffee, None],
        [Nightclub, Home, None, Italian, None],
        [None, None, None, None, None],
        [Gas, Taco, Theatre, None, None]
    ],
    "direction": Direction.R
}

ryan_3 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, True, True, False, True],
        [True, True, True, True, True],
        [True, True, False, True, True],
        [False, True, True, True, True],
        [False, True, True, True, True],
        [False, False, True, False, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, False, True, True, True],
        [True, False, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, False, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, Airport, Gas, None],
        [None, None, Fair, Home, Nightclub],
        [None, Juice, None, None, Taco],
        [Theatre, Flower, None, None, Italian],
        [None, None, None, None, None],
        [None, None, Gas, Coffee, Ballroom],
        [Sandwich, None, None, None, Gas]
    ],
    "direction": Direction.R
}

joe_4 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, False, True, True, True],
        [True, False, True, True, True],
        [True, False, False, True, True],
        [False, True, False, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, False, False, True, True],
        [True, False, False, True, True, True],
        [True, True, True, False, False, True],
        [True, True, True, False, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, Fair, Italian, None],
        [None, Juice, None, None, None],
        [Ballroom, None, None, None, None],
        [Home, Theatre, None, Gas, None],
        [None, Nightclub, Gas, None, Coffee],
        [Airport, Flower, None, None, None],
        [Sandwich, Gas, None, None, Taco]
    ],
    "direction": Direction.L
}

andy_1 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, False, False, True, True],
        [True, False, True, True, True],
        [True, True, False, True, True],
        [False, True, True, True, True],
        [True, False, True, True, True],
        [True, False, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, False, True],
        [True, True, True, False, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, Flower, Italian, None],
        [None, Fair, None, Nightclub, None],
        [Gas, Theatre, Sandwich, None, None],
        [Coffee, None, Ballroom, None, Gas],
        [None, Taco, None, None, Gas],
        [None, None, Juice, None, None],
        [None, Home, Airport, None, None]
    ],
    "direction": Direction.R,
    "gained": (48, 48)
}

joe_5 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [False, False, False, False, True],
        [False, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, False, True],
        [True, True, True, False, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, False, False, False, False, True],
        [True, False, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, None, Taco, None, None],
        [None, None, None, Gas, Juice],
        [None, Ballroom, None, None, None],
        [Home, None, None, None, None],
        [None, Airport, None, Sandwich, None],
        [Flower, Gas, Theatre, Fair, Italian],
        [Nightclub, None, Coffee, Gas, None]
    ],
    "direction": Direction.L
}

andy_2 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, False, True],
        [False, True, False, True, True],
        [False, False, False, True, True],
        [True, False, False, False, True],
        [True, True, False, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
        [True, True, True, True, True, True],
        [True, False, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [Home, Gas, Gas, None, Flower],
        [Gas, Coffee, None, None, None],
        [Italian, None, None, None, None],
        [None, None, None, None, Ballroom],
        [Sandwich, Fair, None, Taco, None],
        [Nightclub, Juice, None, None, Theatre],
        [None, Airport, None, None, None]
    ],
    "direction": Direction.L,
    "gained": (40, 40)
}

stephen_8 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, False, True, True],
        [False, False, True, True, True],
        [False, False, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, False, True, True, True, True],
        [True, True, True, True, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, False, True],
        [True, False, True, False, True, True],
        [True, True, True, True, False, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [None, Nightclub, None, None, None],
        [Juice, None, Gas, Theatre, None],
        [Taco, None, None, Airport, Gas],
        [Italian, None, None, None, Ballroom],
        [Home, None, Fair, None, None],
        [Flower, None, None, None, Gas],
        [Sandwich, None, None, None, Coffee]
    ],
    "direction": Direction.L,
    "ap": 42
}

joe_6 = {
    "horizontal_roads": [
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, True, True, True],
        [True, True, False, False, True],
        [True, True, True, True, True],
    ],
    "vertical_roads": [
        [True, True, False, True, True, True],
        [True, True, False, True, True, True],
        [True, False, False, False, True, True],
        [True, True, False, True, False, True],
        [True, True, True, True, False, True],
        [True, False, True, True, True, True],
        [True, True, True, True, True, True],
    ],
    "board_spaces": [
        [Sandwich, Gas, Fair, Italian, Ballroom],
        [Gas, Theatre, Airport, None, None],
        [None, None, None, None, None],
        [None, Taco, None, Flower, None],
        [None, None, Home, Juice, None],
        [Nightclub, Gas, None, None, Coffee],
        [None, None, None, None, None]
    ],
    "direction": Direction.L
}

board = joe_6

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
