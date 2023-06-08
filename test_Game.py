import Game
import pytest

test_is_empty = [
    (True, []),  # EMPTY FRAME
    (False, [0]),  # Single GUTTERBALL
    (False, [0, 0]),  # Double GUTTERBALL
    (False, [10]),  # Strike
    (False, [5, 5]),  # Spare
    (True, None),  # Spare
]


@pytest.mark.parametrize("true_false, frame_data", test_is_empty)
def test_is_empty(true_false, frame_data):
    assert Game.Game.is_empty(frame_data=frame_data) == true_false


test_is_gutter = [
    (True, []),  # EMPTY FRAME
    (True, [0]),  # Single GUTTERBALL
    (True, [0, 0]),  # Double GUTTERBALL
    (False, [10]),  # Strike
    (False, [5, 5]),  # Spare
    (True, None),  # Spare
]


@pytest.mark.parametrize("true_false, frame_data", test_is_gutter)
def test_is_gutter(true_false, frame_data):
    assert Game.Game.is_gutter(frame_data=frame_data) == true_false


test_is_strike = [
    (False, []),  # EMPTY FRAME
    (False, [0]),  # Single GUTTERBALL
    (False, [0, 0]),  # Double GUTTERBALL
    (True, [10]),  # Strike
    (False, [5, 5]),  # Spare
    (False, None),  # Spare
]


@pytest.mark.parametrize("true_false, frame_data", test_is_strike)
def test_is_strike(true_false, frame_data):
    assert Game.Game.is_strike(frame_data=frame_data) == true_false


test_is_spare = [
    (False, []),  # EMPTY FRAME
    (False, [0]),  # Single GUTTERBALL
    (False, [0, 0]),  # Double GUTTERBALL
    (False, [10]),  # Strike
    (True, [5, 5]),  # Spare
    (False, None),  # Spare
]


@pytest.mark.parametrize("true_false, frame_data", test_is_spare)
def test_is_spare(true_false, frame_data):
    assert Game.Game.is_spare(frame_data=frame_data) == true_false


test_data_score = [
    (0,     0,  [[], [], [], [], [], [], [], [], [], []]),  # EMPTY GAME
    (0,     0,  [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),  # Total Loser
    (30,    0,  [[10], [10], [10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),  # Turkey
    (30,    1,  [[0, 0], [10], [10], [10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),  # Later Turkey
    (30,    10, [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 10, 10]]),  # Last Turkey
    (60,    5,  [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]]),
    # Perfect Game
    (0, 0, None),
]


@pytest.mark.parametrize("score, frame, frame_data", test_data_score)
def test_get_frame_score(score, frame, frame_data):
    g = Game.Game(frame_data)
    assert g.get_frame_score(frame) == score


def test_roll():
    assert False


def test_update_score():
    assert False


def test_score():
    assert False


def test_print(capsys):
    g = Game.Game()
    g.print()
    out, err = capsys.readouterr()
    assert out == "The Array is: [[], [], [], [], [], [], [], [], [], []]\n"
