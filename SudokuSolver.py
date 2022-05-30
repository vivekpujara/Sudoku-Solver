# Add cosmetic separator lines to boards. Add print board function too? (YouTube)
# Add stepwise print of each array produced by backtracking. (YouTube)

# Sudoku Solver code using backtracking algorithm with recursion.

# Import NumPy module/library for vertically orienting array representing Sudoku board.
import numpy as np

# Import native Time module/library for displaying program runtime.
import time

# Function to search for next element to fill.
def find_next_box_to_fill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

# Function to check if valid.
def is_valid(grid, i, j, s):
    row_ok = all([s != grid[i][x] for x in range(9)])
    if row_ok:
        column_ok = all([s != grid[x][j] for x in range(9)])
        if column_ok:
            top_x_section, top_y_section = 3 * (i // 3), 3 * (j // 3)
            for x in range(top_x_section, top_x_section + 3):
                for y in range(top_y_section, top_y_section + 3):
                    if grid[x][y] == s:
                        return False
            return True
    return False

# Sudoku solving function.
def solve_sudoku(grid, i=0, j=0):
    i, j = find_next_box_to_fill(grid, i, j)
    if i == -1:
        return True
    for s in range(1, 10):
        if is_valid(grid, i, j, s):
            grid[i][j] = s
            if solve_sudoku(grid, i, j):
                return "Sudoku has been solved!"
            # Triggers backtracking.
            grid[i][j] = 0
    return False

# Sample input of starting Sudoku board.
# test1 = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
#        [2, 8, 9, 0, 0, 4, 0, 0, 0],
#        [3, 4, 6, 2, 0, 5, 0, 9, 0],
#        [6, 0, 2, 0, 0, 0, 0, 1, 0],
#        [0, 3, 8, 0, 0, 6, 0, 4, 7],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 9, 0, 0, 0, 0, 0, 7, 8],
#        [7, 0, 3, 4, 0, 0, 5, 6, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

test = [[0, 0, 0, 0, 7, 0, 3, 2, 0],
        [0, 0, 8, 0, 2, 0, 5, 1, 6],
        [0, 4, 5, 0, 0, 1, 8, 0, 0],
        [0, 1, 0, 0, 0, 6, 7, 0, 0],
        [8, 0, 6, 0, 1, 0, 4, 0, 2],
        [0, 0, 7, 4, 0, 0, 0, 8, 0],
        [0, 0, 9, 3, 0, 0, 2, 4, 0],
        [3, 7, 4, 0, 5, 0, 9, 0, 0],
        [0, 8, 2, 0, 4, 0, 0, 0, 0]]

# Display output, confirmation statement, vertically oriented array as solved Sudoku board, and program runtime.
print(solve_sudoku(test))
print("Solved board:")
print(np.array(test))
start_time = time.time()
print("Runtime:")
print("--- %s seconds ---" % (time.time() - start_time))
