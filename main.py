from maze import Maze
from window import Window

def main():
    win = Window(800, 700)

    # Create a randomly generated maze and solve it.
    maze = Maze(50, 50, 12, 14, 50, 50, win)

    maze.solve()

    win.wait_for_close()


main()
