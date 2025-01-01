from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    # Test drawing cells and moves from one cell to another
    #maze = Maze(50, 50, 5, 5, 75, 75, win)
    maze = Maze(50, 50, 6, 8, 75, 75, win)

    win.wait_for_close()


main()
