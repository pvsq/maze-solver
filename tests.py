import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


    def test_maze_with_no_cols_or_rows(self):
        num_cols = 0
        num_rows = 0
        # It shouldn't be possible to create a maze with
        # zero rows and zero columns.
        with self.assertRaises(IndexError):
            Maze(50, 50, num_rows, num_cols, 75, 75)


    def test_maze_with_one_cell(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )


    def test_maze_removed_top_wall_on_first_cell(self):
        num_cols = 8
        num_rows = 6
        m1 = Maze(50, 50, num_rows, num_cols, 75, 75)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )


    def test_maze_removed_bottom_wall_on_last_cell(self):
        num_cols = 8
        num_rows = 6
        m1 = Maze(50, 50, num_rows, num_cols, 75, 75)
        self.assertEqual(
            m1._cells[m1.num_cols-1][m1.num_rows-1].has_bottom_wall,
            False,
        )


    def test_maze_reset_cells_visited(self):
        num_cols = 14
        num_rows = 12
        m1 = Maze(50, 50, num_rows, num_cols, 50, 50, seed=37431)
        visited_count = 0
        actual_count = 0
        for i in range(num_cols):
            for j in range(num_rows):
                if m1._cells[i][j].visited == True:
                    actual_count += 1
        self.assertEqual(visited_count, actual_count)



if __name__ == "__main__":
    unittest.main()
