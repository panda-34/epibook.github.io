import math


# @include
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    n = len(partial_assignment)
    # Check row constraints.
    if any(has_duplicate(partial_assignment, i, i + 1, 0, n)
           for i in range(n)):
        return False

    # Check column constraints.
    if any(has_duplicate(partial_assignment, 0, n, j, j + 1)
           for j in range(n)):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return not any(
        has_duplicate(partial_assignment, region_size * I, region_size *
                      (I + 1), region_size * J, region_size * (J + 1))
        for I in range(region_size) for J in range(region_size))


# Return True if subarray partial_assignment[start_row : end_row - 1][start_col : end_col - 1] contains any duplicates in {1, 2, ..., len(partial_assignment)}; otherwise return False.
def has_duplicate(partial_assignment, start_row, end_row, start_col, end_col):
    is_present = [False] * (len(partial_assignment) + 1)
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if partial_assignment[i][j] != 0 and is_present[partial_assignment[
                    i][j]]:
                return True
            is_present[partial_assignment[i][j]] = True
    return False
# @exclude


def main():
    A = [[0, 2, 6, 0, 0, 0, 8, 1, 0], [3, 0, 0, 7, 0, 8, 0, 0, 6],
         [4, 0, 0, 0, 5, 0, 0, 0, 7], [0, 5, 0, 1, 0, 7, 0, 9, 0],
         [0, 0, 3, 9, 0, 5, 1, 0, 0], [0, 4, 0, 3, 0, 2, 0, 5, 0],
         [1, 0, 0, 0, 3, 0, 0, 0, 2], [5, 0, 0, 2, 0, 4, 0, 0, 9],
         [0, 3, 8, 0, 0, 0, 4, 6, 0]]
    assert is_valid_sudoku(A)
    A[-1] = [3, 3, 8, 0, 0, 0, 4, 6, 0]
    assert not is_valid_sudoku(A)


if __name__ == '__main__':
    main()
