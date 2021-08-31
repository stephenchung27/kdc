from enum import Enum


class Direction(Enum):
    U = "UP"
    D = "DOWN"
    L = "LEFT"
    R = "RIGHT"


class BoardSpaceType(Enum):
    G = "Gas Station"
    P = "Italian"           # P for sPaghetti
    T = "Taco"
    S = "Sandwich Shop"
    F = "Fair"
    J = "Juice"
    C = "Coffee"
    N = "Nightclub"
    L = "Flower Garden"     # L for fLower garden
    B = "Ballroom"
    R = "Theatre"           # R for theatRe
    A = "Airport"
    E = "Jewelry Store"     # E for jEwelry store
    M = "Shopping Mall"     # M for Mall
    H = "Home"
