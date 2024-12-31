from cell import Cell
from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    # Test drawing cells and moves from one cell to another
    c1 = Cell(50, 100, 100, 150, win,
              has_left_wall=True, has_top_wall=True,
              has_right_wall=False, has_bottom_wall=False)
    c1.draw()
    c2 = Cell(50, 100, 400, 450, win,
              has_left_wall=True, has_top_wall=False,
              has_right_wall=True, has_bottom_wall=True)
    c2.draw()
    c3 = Cell(500, 550, 100, 150, win,
              has_left_wall=False, has_top_wall=True,
              has_right_wall=True, has_bottom_wall=True)
    c3.draw()

    c1.draw_move(c2, undo=False)
    c3.draw_move(c1, undo=True)
    c2.draw_move(c3, undo=False)

    win.wait_for_close()


main()
