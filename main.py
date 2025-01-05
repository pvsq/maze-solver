from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window

def main():
    win = Window(800, 700)

    # Test drawing a randomly generated maze
    #maze = Maze(50, 50, 12, 14, 50, 50, win, 37431)
    Maze(50, 50, 12, 14, 50, 50, win)

    win.wait_for_close()


main()
