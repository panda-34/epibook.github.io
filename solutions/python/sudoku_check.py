import math


# @include
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
            has_duplicate([partial_assignment[i][j] for j in range(n)]) or
            has_duplicate([partial_assignment[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(not has_duplicate([
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))


# Return True if subarray partial_assignment[start_row : end_row - 1][start_col : end_col - 1] contains any duplicates in {1, 2, ..., len(partial_assignment)}; otherwise return False.
def has_duplicate(block):
    block = list(filter(lambda x: x != 0, block))
    return len(block) != len(set(block))


# @exclude

import collections


def is_valid_sudoku_pythonic(partial_assignment):
    return max(
        list(
            collections.Counter(
                k
                for i, row in enumerate(partial_assignment)
                for j, c in enumerate(row)
                if c != 0 for k in ((i, c), (c, j), (i / int(
                    math.sqrt(len(partial_assignment))), j / int(
                        math.sqrt(len(partial_assignment))), c)))
            .values()) + [0]) <= 1


def main():
    A = [[0, 2, 6, 0, 0, 0, 8, 1, 0], [3, 0, 0, 7, 0, 8, 0, 0, 6],
         [4, 0, 0, 0, 5, 0, 0, 0, 7], [0, 5, 0, 1, 0, 7, 0, 9, 0],
         [0, 0, 3, 9, 0, 5, 1, 0, 0], [0, 4, 0, 3, 0, 2, 0, 5, 0],
         [1, 0, 0, 0, 3, 0, 0, 0, 2], [5, 0, 0, 2, 0, 4, 0, 0, 9],
         [0, 3, 8, 0, 0, 0, 4, 6, 0]]
    assert is_valid_sudoku(A)
    #assert is_valid_sudoku_pythonic(A)
    A[-1] = [3, 3, 8, 0, 0, 0, 4, 6, 0]
    assert not is_valid_sudoku(A)
    #assert not is_valid_sudoku_pythonic(A)
    A = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert is_valid_sudoku_pythonic(A)


if __name__ == '__main__':
    main()
