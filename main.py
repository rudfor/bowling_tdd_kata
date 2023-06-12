#!/usr/bin/env python
import Game
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    g = Game.Game()
    g.print()
    g.print_score()
    g2 = Game.Game([[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [10, 10, 10]])
    g2.print()
    g2.print_score()
    g2 = Game.Game([[10], [10], [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
    g2.print()
    g2.print_score()
    assert (g.score == 0)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
