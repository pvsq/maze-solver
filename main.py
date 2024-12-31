from line import Line
from point import Point
from window import Window

def main():
    win = Window(800, 600)

    # Test drawing some lines
    win.draw_line(Line(Point(50, 20), Point(90, 100)), "black")
    win.draw_line(Line(Point(150, 20), Point(450, 600)), "red")
    win.draw_line(Line(Point(0,0), Point(800,600)), "green")
    win.draw_line(Line(Point(800,0), Point(0,600)), "yellow")

    win.wait_for_close()


main()
