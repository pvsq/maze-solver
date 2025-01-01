import time
from cell import Cell


class Maze:
    def __init__(
            self,
            x1, y1,
            num_rows,
            num_cols,
            cell_size_x, cell_size_y,
            win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()


    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            start_x = self.x1 + self.cell_size_x * i
            row = []
            for j in range(self.num_rows):
                start_y = self.y1 + self.cell_size_y * j
                c = Cell(
                    start_x, start_x + self.cell_size_x,
                    start_y, start_y + self.cell_size_y,
                    self.win
                )
                row.append(c)
            self._cells.append(row)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

        self._break_entrance_and_exit()


    def _break_entrance_and_exit(self):
        if self.num_rows==0 and self.num_cols==0:
            return
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        bot_x, bot_y = self.num_rows-1, self.num_cols-1
        self._cells[bot_y][bot_x].has_bottom_wall = False
        self._cells[bot_y][bot_x].draw()


    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()


    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

