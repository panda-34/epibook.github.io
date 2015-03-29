# Sudoku_solve.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import math
from sudoku_check import is_valid_sudoku


# @include
def solve_sudoku(A):
    if not is_valid_sudoku(A):
        print('Initial configuration violates constraints.')
        return False

    if solve_sudoku_helper(0, 0, A):
        for i in A:
            print(*i)
        return True
    else:
        print('No solution exists.')
        return False


def solve_sudoku_helper(i, j, A):
    if i == len(A):
        i = 0  # Starts a row.
        j += 1
        if j == len(A[i]):
            return True  # Entire matrix has been filled without conflict.

    # Skips nonempty entries.
    if A[i][j] != 0:
        return solve_sudoku_helper(i + 1, j, A)

    for val in range(1, len(A) + 1):
        # Note: practically, it's substantially quicker to check if entry val
        # conflicts with any of the constraints if we add it at (i,j) before
        # adding it, rather than adding it and then calling is_valid_Sudoku.
        # The reason is that we know we are starting with a valid configuration,
        # and the only entry which can cause a problem is entryval at (i,j).
        if valid_to_add(A, i, j, val):
            A[i][j] = val
            if solve_sudoku_helper(i + 1, j, A):
                return True

    A[i][j] = 0  # Undo assignment.
    return False


def valid_to_add(A, i, j, val):
    # Check row constraints.
    for k in range(len(A)):
        if val == A[k][j]:
            return False

    # Check column constraints.
    if val in A[i]:
        return False

    # Check region constraints.
    region_size = int(math.sqrt(len(A)))
    I = i // region_size
    J = j // region_size
    for a in range(region_size):
        for b in range(region_size):
            if val == A[region_size * I + a][region_size * J + b]:
                return False

    return True
# @exclude


def main():
    A = [[0, 2, 6, 0, 0, 0, 8, 1, 0],
         [3, 0, 0, 7, 0, 8, 0, 0, 6],
         [4, 0, 0, 0, 5, 0, 0, 0, 7],
         [0, 5, 0, 1, 0, 7, 0, 9, 0],
         [0, 0, 3, 9, 0, 5, 1, 0, 0],
         [0, 4, 0, 3, 0, 2, 0, 5, 0],
         [1, 0, 0, 0, 3, 0, 0, 0, 2],
         [5, 0, 0, 2, 0, 4, 0, 0, 9],
         [0, 3, 8, 0, 0, 0, 4, 6, 0]]
    solve_sudoku(A)
    golden_A = [[7, 2, 6, 4, 9, 3, 8, 1, 5],
                [3, 1, 5, 7, 2, 8, 9, 4, 6],
                [4, 8, 9, 6, 5, 1, 2, 3, 7],
                [8, 5, 2, 1, 4, 7, 6, 9, 3],
                [6, 7, 3, 9, 8, 5, 1, 2, 4],
                [9, 4, 1, 3, 6, 2, 7, 5, 8],
                [1, 9, 4, 8, 3, 6, 5, 7, 2],
                [5, 6, 7, 2, 1, 4, 3, 8, 9],
                [2, 3, 8, 5, 7, 9, 4, 6, 1]]
    assert A == golden_A


if __name__ == '__main__':
    main()
