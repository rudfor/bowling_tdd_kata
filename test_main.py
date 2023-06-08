from unittest import TestCase
import Game
import pytest

test_data = [
    (0,     [[], [], [], [], [], [], [], [], [], []]),  # EMPTY GAME
    (False, [[], [], [], [], [], [], [], [], []]),  # Invalid Frame
    (0,     [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),  # Total Loser
    (60,    [[10], [10], [10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),  # Turkey
    (60,    [[0, 0], [10], [10], [10], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]),  # Later Turkey
    (30,    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 10, 10]]),  # Last Turkey
    (300,    [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]]),
    # Perfect Game
    (0, None),
]


@pytest.mark.parametrize("score, score_array", test_data)
def test_score(score, score_array):
    if type(score) is int:
        g = Game.Game(score_array)
        assert (g.score == score)
    else:
        try:
            g = Game.Game(score_array)
            assert not score
        except Exception as E:
            print(f"Exception {E}")
            assert not score


testDataRolls = [
    (0, [0] * 20),  # EMPTY GAME
    (0, ([0] * 10) + ([10] * 5)),  # EMPTY GAME
    ]

@pytest.mark.parametrize("score, rolls", testDataRolls)
def test_score_rolls(score, rolls):
    g = Game.Game()
    for i in rolls:
        g.roll(i)
    print(g)



class TestGame(TestCase):
    def test_roll(self):
        self.assertTrue(True)

    def test_print(self):
        self.assertTrue(True)
