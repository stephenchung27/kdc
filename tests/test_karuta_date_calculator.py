from karuta_date_calculator import KarutaDateCalculator
from constants import Direction


def test_karuta_date_calculator(filled_json_board):
    kdc = KarutaDateCalculator()
    kdc(filled_json_board, Direction.L)

    assert kdc.possible_routes
