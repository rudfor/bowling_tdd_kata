from unittest import TestCase
import Game
import pytest

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



# class TestGame(TestCase):
#     def test_roll(self):
#         self.assertTrue(True)
#
#     def test_print(self):
#         self.assertTrue(True)
