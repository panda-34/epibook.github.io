# String_in_matrix.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def is_pattern_contained_in_grid(grid, S):
    # Each entry in previous_attempts is a point in the grid and suffix of pattern (identified by its offset). Presence in previous_attempts indicates the suffix is not contained in the grid starting from that point.
    previous_attempts = set()
    return any(
        is_pattern_suffix_contained_starting_at_xy(grid, S, i, j, 0,
                                                   previous_attempts)
        for i in range(len(grid)) for j in range(len(grid[i])))


def is_pattern_suffix_contained_starting_at_xy(grid, S, x, y, length,
                                               previous_attempts):
    if len(S) == length:
        # Nothing left to complete.
        return True

    # Check if (x, y) lies outside the grid.
    if not 0 <= x < len(grid) or not 0 <= y < len(grid[x]) or (
            x, y, length) in previous_attempts:
        return False

    if grid[x][y] == S[length] and is_pattern_suffix_contained_starting_at_xy(
            grid, S, x - 1, y, length + 1,
            previous_attempts) or is_pattern_suffix_contained_starting_at_xy(
                grid, S, x + 1, y, length + 1, previous_attempts
            ) or is_pattern_suffix_contained_starting_at_xy(
                grid, S, x, y - 1, length + 1, previous_attempts
            ) or is_pattern_suffix_contained_starting_at_xy(
                grid, S, x, y + 1, length + 1, previous_attempts):
        return True
    previous_attempts.add((x, y, length))
    return False


# @exclude


def main():
    n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(2, 10)
    A = [[random.randrange(n) for j in range(n)] for i in range(n)]
    for a in A:
        print(*a)
    print('S = ', end='')
    S = [random.randrange(n) for i in range(1 + random.randint(1, n * n // 2))]
    print(*S)
    print(is_pattern_contained_in_grid(A, S))


if __name__ == '__main__':
    main()
