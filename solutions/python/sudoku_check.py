import math


# @include
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(A):
    # Check row constraints.
    for i in range(len(A)):
        if has_duplicate(A, i, i + 1, 0, len(A), len(A)):
            return False

    # Check column constraints.
    for j in range(len(A)):
        if has_duplicate(A, 0, len(A), j, j + 1, len(A)):
            return False

    # Check region constraints.
    region_size = int(math.sqrt(len(A)))
    for I in range(region_size):
        for J in range(region_size):
            if has_duplicate(A, region_size * I, region_size * (I + 1),
                             region_size * J, region_size * (J + 1), len(A)):
                return False

    return True


# Return True if subarray A[start_row : end_row - 1][start_col : end_col - 1]
# contains any duplicates in [1 : num_elements]; otherwise return False.
def has_duplicate(A, start_row, end_row, start_col, end_col, num_elements):
    is_present = [False] * (num_elements + 1)
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if A[i][j] != 0 and is_present[A[i][j]]:
                return True
            is_present[A[i][j]] = True
    return False
# @exclude
