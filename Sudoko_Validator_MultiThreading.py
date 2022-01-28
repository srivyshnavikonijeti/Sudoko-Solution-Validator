

from itertools import product
from threading import Thread
from timeit import default_timer as timer
import queue

DIGITS = set(range(1, 10))


def check_grid_size(grid):
    """Check that the grid is 9x9."""
    well_formed = len(grid) == 9 and all(len(row) == 9 for row in grid)
    return well_formed or None


def check_rows(grid, q):
    """Check that each number appears exactly once per row."""
    q.put(all(set(row) == DIGITS for row in grid))


def check_columns(grid, q):
    """Check that each number appears exactly once per column."""
    columns = [[row[c] for row in grid] for c in range(9)]
    q.put(all(set(col) == DIGITS for col in columns))


def check_3x3_grid(grid, q):
    """Check that each number appears exactly once per 3x3 grid."""
    threes = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    for row_block, col_block in product(threes, threes):
        block = [grid[r][c] for r, c in product(row_block, col_block)]
        if set(block) != DIGITS:
            q.put(False)
            return

    q.put(True)


def check_sudoku(grid):
    """
    Validate a sudoku solution.

    Given a grid as a list of lists, return None if it is ill-formed,
    False if it is invalid, or True if it is a valid solution.
    """
    assert isinstance(grid, list)

    q = queue.Queue()

    if not check_grid_size(grid):
        return None

    row_thread = Thread(target=check_rows, args=(grid, q))
    row_thread.start()

    columns_thread = Thread(target=check_columns, args=(grid, q))
    columns_thread.start()

    grid_threads = []
    for _ in range(9):
        t = Thread(target=check_3x3_grid, args=(grid, q))
        t.start()
        grid_threads.append(t)

    row_thread.join()
    columns_thread.join()

    [t.join() for t in grid_threads]

    results = []
    while not q.empty():
        results.append(q.get())

    return all(results)


def main():
    ill_formed = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                  [6, 7, 2, 1, 9, 5, 3, 4, 8],
                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
                  [8, 5, 9, 7, 6, 1, 4, 2, 3],
                  [4, 2, 6, 8, 5, 3, 7, 9],  # <---
                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                  [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # check_sudoku should return True
    valid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
             [6, 7, 2, 1, 9, 5, 3, 4, 8],
             [1, 9, 8, 3, 4, 2, 5, 6, 7],
             [8, 5, 9, 7, 6, 1, 4, 2, 3],
             [4, 2, 6, 8, 5, 3, 7, 9, 1],
             [7, 1, 3, 9, 2, 4, 8, 5, 6],
             [9, 6, 1, 5, 3, 7, 2, 8, 4],
             [2, 8, 7, 4, 1, 9, 6, 3, 5],
             [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    # check_sudoku should return False
    invalid = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
               [6, 7, 2, 1, 9, 5, 3, 4, 8],
               [1, 9, 8, 3, 8, 2, 5, 6, 7],
               [8, 5, 9, 7, 6, 1, 4, 2, 3],
               [4, 2, 6, 8, 5, 3, 7, 9, 1],
               [7, 1, 3, 9, 2, 4, 8, 5, 6],
               [9, 6, 1, 5, 3, 7, 2, 8, 4],
               [2, 8, 7, 4, 1, 9, 6, 3, 5],
               [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    print(check_sudoku(valid))
    print(check_sudoku(invalid))
    print(check_sudoku(ill_formed))


if __name__ == '__main__':
    main()