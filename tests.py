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
        m1 = Maze(50, 50, num_rows, num_cols, 75, 75)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        with self.assertRaises(IndexError):
            m1._cells[0]


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


if __name__ == "__main__":
    unittest.main()
