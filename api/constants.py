from enum import Enum


class Direction(Enum):
    U = "Up"
    D = "Down"
    L = "Left"
    R = "Right"


class BoardSpaceType(Enum):
    G = "Gas Station"
    P = "Italian Restaurant"    # P for sPaghetti
    T = "Taco Stand"
    S = "Sandwich Shop"
    F = "Fair"
    J = "Juice Bar"
    C = "Coffee House"
    N = "Nightclub"
    L = "Flower Garden"         # L for fLower garden
    B = "Ballroom"
    R = "Theatre"               # R for theatRe
    A = "Airport"
    E = "Jewelry Store"         # E for jEwelry store
    M = "Shopping Mall"         # M for Mall
    H = "Home"
