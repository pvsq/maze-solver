from line import Line
from point import Point


class Cell:
    def __init__(
        self, 
        x1, x2, y1, y2,
        win=None,
        has_left_wall=True, has_right_wall=True,
        has_top_wall=True, has_bottom_wall=True
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win


    def draw(self):
        if self._win is None:
            return
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
                    "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)),
                    "white"
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
                    "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)),
                    "white"
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
                    "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)),
                    "white"
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
                    "black"
            )
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)),
                    "white"
            )


    def draw_move(self, to_cell, undo=False):
        mid_x_self = self._x1 + (1/2) * (abs(self._x2 - self._x1))
        mid_y_self = self._y1 + (1/2) * (abs(self._y2 - self._y1))
        mid_x_to = to_cell._x1 + (1/2) * (abs(to_cell._x2 - to_cell._x1))
        mid_y_to = to_cell._y1 + (1/2) * (abs(to_cell._y2 - to_cell._y1))
        l = Line(Point(mid_x_self, mid_y_self), Point(mid_x_to, mid_y_to))
        fill_color = "red"
        if undo:
            fill_color = "gray"
        if self._win is None:
            return
        self._win.draw_line(l, fill_color)

