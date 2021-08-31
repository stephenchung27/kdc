from pytest import fixture
from unittest.mock import MagicMock
from constants import Direction, BoardSpaceType
from board_parser import BoardParser


@fixture
def blank_board_parser(blank_json_board):
    return BoardParser(blank_json_board)


@fixture
def board_parser_with_json(filled_json_board):
    return BoardParser(filled_json_board)


def test_setup_roads_horizontal_roads(blank_board_parser):
    bp = blank_board_parser

    # Top left horizontal road
    assert len(bp.horizontal_roads[0][0][Direction.L]) == 1
    assert bp.vertical_roads[0][0] in [
        action.action for action in bp.horizontal_roads[0][0][Direction.L]]

    assert len(bp.horizontal_roads[0][0][Direction.R]) == 2
    assert bp.vertical_roads[0][1] in [
        action.action for action in bp.horizontal_roads[0][0][Direction.R]]
    assert bp.horizontal_roads[0][1] in [
        action.action for action in bp.horizontal_roads[0][0][Direction.R]]

    # Top right horizontal road
    assert len(bp.horizontal_roads[0][-1][Direction.L]) == 2
    assert bp.horizontal_roads[0][-2] in [
        action.action for action in bp.horizontal_roads[0][-1][Direction.L]]
    assert bp.vertical_roads[0][-2] in [
        action.action for action in bp.horizontal_roads[0][-1][Direction.L]]

    assert len(bp.horizontal_roads[0][-1][Direction.R]) == 1
    assert bp.vertical_roads[0][-1] in [
        action.action for action in bp.horizontal_roads[0][-1][Direction.R]]

    # Bottom left horizontal road
    assert len(bp.horizontal_roads[-1][0][Direction.L]) == 1
    assert bp.vertical_roads[-1][0] in [
        action.action for action in bp.horizontal_roads[-1][0][Direction.L]]

    assert len(bp.horizontal_roads[-1][0][Direction.R]) == 2
    assert bp.vertical_roads[-1][1] in [
        action.action for action in bp.horizontal_roads[-1][0][Direction.R]]
    assert bp.vertical_roads[-1][1] in [
        action.action for action in bp.horizontal_roads[-1][0][Direction.R]]

    # Bottom left horizontal road
    assert len(bp.horizontal_roads[-1][-1][Direction.L]) == 2
    assert bp.horizontal_roads[-1][-2] in [
        action.action for action in bp.horizontal_roads[-1][-1][Direction.L]]
    assert bp.vertical_roads[-1][-2] in [
        action.action for action in bp.horizontal_roads[-1][-1][Direction.L]]

    assert len(bp.horizontal_roads[-1][-1][Direction.R]) == 1
    assert bp.vertical_roads[-1][-1] in [
        action.action for action in bp.horizontal_roads[-1][-1][Direction.R]]

    # Middle horizontal road
    assert len(bp.horizontal_roads[2][2][Direction.L]) == 3
    assert bp.horizontal_roads[2][1] in [
        action.action for action in bp.horizontal_roads[2][2][Direction.L]]
    assert bp.vertical_roads[1][2] in [
        action.action for action in bp.horizontal_roads[2][2][Direction.L]]
    assert bp.vertical_roads[2][2] in [
        action.action for action in bp.horizontal_roads[2][2][Direction.L]]

    assert len(bp.horizontal_roads[2][2][Direction.R]) == 3
    assert bp.horizontal_roads[2][3] in [
        action.action for action in bp.horizontal_roads[2][2][Direction.R]]
    assert bp.vertical_roads[1][3] in [
        action.action for action in bp.horizontal_roads[2][2][Direction.R]]
    assert bp.vertical_roads[2][3] in [
        action.action for action in bp.horizontal_roads[2][2][Direction.R]]


def test_setup_roads_vertical_roads(blank_board_parser):
    bp = blank_board_parser

    # Top left vertical road
    assert len(bp.vertical_roads[0][0][Direction.U]) == 1
    assert bp.horizontal_roads[0][0] in [
        action.action for action in bp.vertical_roads[0][0][Direction.U]]

    assert len(bp.vertical_roads[0][0][Direction.D]) == 2
    assert bp.vertical_roads[1][0] in [
        action.action for action in bp.vertical_roads[0][0][Direction.D]]
    assert bp.horizontal_roads[1][0] in [
        action.action for action in bp.vertical_roads[0][0][Direction.D]]

    # Top right vertical road
    assert len(bp.vertical_roads[0][-1][Direction.U]) == 1
    assert bp.horizontal_roads[0][-1] in [
        action.action for action in bp.vertical_roads[0][-1][Direction.U]]

    assert len(bp.vertical_roads[0][-1][Direction.D]) == 2
    assert bp.vertical_roads[1][-1] in [
        action.action for action in bp.vertical_roads[0][-1][Direction.D]]
    assert bp.horizontal_roads[1][-1] in [
        action.action for action in bp.vertical_roads[0][-1][Direction.D]]

    # Bottom left vertical road
    assert len(bp.vertical_roads[-1][0][Direction.U]) == 2
    assert bp.horizontal_roads[-2][0] in [
        action.action for action in bp.vertical_roads[-1][0][Direction.U]]
    assert bp.vertical_roads[-2][0] in [
        action.action for action in bp.vertical_roads[-1][0][Direction.U]]

    assert len(bp.vertical_roads[-1][0][Direction.D]) == 1
    assert bp.horizontal_roads[-1][0] in [
        action.action for action in bp.vertical_roads[-1][0][Direction.D]]

    # Bottom right vertical road
    assert len(bp.vertical_roads[-1][-1][Direction.U]) == 2
    assert bp.horizontal_roads[-2][-1] in [
        action.action for action in bp.vertical_roads[-1][-1][Direction.U]]
    assert bp.vertical_roads[-2][-1] in [
        action.action for action in bp.vertical_roads[-1][-1][Direction.U]]

    assert len(bp.vertical_roads[-1][-1][Direction.D]) == 1
    assert bp.horizontal_roads[-1][-1] in [
        action.action for action in bp.vertical_roads[-1][-1][Direction.D]]

    # Middle vertical road
    assert len(bp.vertical_roads[3][4][Direction.U]) == 3
    assert bp.horizontal_roads[3][3] in [
        action.action for action in bp.vertical_roads[3][4][Direction.U]]
    assert bp.horizontal_roads[3][4] in [
        action.action for action in bp.vertical_roads[3][4][Direction.U]]
    assert bp.vertical_roads[2][4] in [
        action.action for action in bp.vertical_roads[3][4][Direction.U]]

    assert len(bp.vertical_roads[3][4][Direction.D]) == 3
    assert bp.horizontal_roads[4][3] in [
        action.action for action in bp.vertical_roads[3][4][Direction.D]]
    assert bp.horizontal_roads[4][4] in [
        action.action for action in bp.vertical_roads[3][4][Direction.D]]
    assert bp.vertical_roads[4][4] in [
        action.action for action in bp.vertical_roads[3][4][Direction.D]]


def test_parse_blocked_roads(board_parser_with_json):
    bp = board_parser_with_json

    # Random horizontal road block
    assert len(bp.horizontal_roads[5][1][Direction.L]) == 2
    assert bp.horizontal_roads[5][0] not in [
        action.action for action in bp.horizontal_roads[5][1][Direction.L]]
    assert bp.vertical_roads[4][1] in [
        action.action for action in bp.horizontal_roads[5][1][Direction.L]]
    assert bp.vertical_roads[5][1] in [
        action.action for action in bp.horizontal_roads[5][1][Direction.L]]

    # Random vertical road block
    assert len(bp.horizontal_roads[5][1][Direction.R]) == 2  # Sanity check
    assert bp.horizontal_roads[5][2] in [
        action.action for action in bp.horizontal_roads[5][1][Direction.R]]
    assert bp.vertical_roads[4][2] not in [
        action.action for action in bp.horizontal_roads[5][1][Direction.R]]
    assert bp.vertical_roads[5][2] in [
        action.action for action in bp.horizontal_roads[5][1][Direction.R]]


def test_parse_board_spaces(board_spaces, board_parser_with_json):
    bp = board_parser_with_json
    mock_direction = MagicMock()

    assert len(bp.vertical_roads[2][1].board_space_actions) == 2
    assert BoardSpaceType(board_spaces[2][0]) in [
        action.action_type for action in bp.vertical_roads[2][1].available_actions(mock_direction, 1)]
    assert BoardSpaceType(board_spaces[2][1]) in [
        action.action_type for action in bp.vertical_roads[2][1].available_actions(mock_direction, 1)]
