from cell import Cell
from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    # Test drawing cells with walls
    c1 = Cell(50, 100, 100, 150, win,
              has_left_wall=True, has_top_wall=False,
              has_right_wall=False, has_bottom_wall=False)
    c1.draw()
    c2 = Cell(100, 150, 150, 200, win)
    c2.draw()
    c3 = Cell(150, 200, 200, 250, win,
              has_left_wall=False, has_top_wall=True,
              has_right_wall=False, has_bottom_wall=True)
    c3.draw()
    c4 = Cell(200, 250, 250, 300, win,
              has_left_wall=False, has_top_wall=False,
              has_right_wall=True, has_bottom_wall=True)
    c4.draw()
    c5 = Cell(250, 300, 300, 350, win,
              has_left_wall=True, has_top_wall=True,
              has_right_wall=False, has_bottom_wall=False)
    c5.draw()

    win.wait_for_close()


main()
