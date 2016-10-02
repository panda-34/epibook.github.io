# n-queens.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def n_queens(n):
    result = []
    placement = []
    solve_n_queens(n, 0, placement, result)
    return result


def solve_n_queens(n, row, col_placement, result):
    if row == n:
        # All queens are legally placed.
        result.append(col_placement.copy())
    else:
        for col in range(n):
            col_placement.append(col)
            if is_valid(col_placement):
                solve_n_queens(n, row + 1, col_placement, result)
            del col_placement[-1]


# Test if a newly placed queen will conflict any earlier queens
# placed before.
def is_valid(col_placement):
    row_id = len(col_placement) - 1
    for i in range(row_id):
        diff = abs(col_placement[i] - col_placement[row_id])
        if diff == 0 or diff == row_id - i:
            # A column or diagonal constraint is violated.
            return False
    return True
# @exclude


def to_text_representation(col_placement):
    sol = []
    for row in col_placement:
        line = ['.'] * len(col_placement)
        line[row] = 'Q'
        sol.append(''.join(line))
    return sol


def simple_test():
    result = n_queens(2)
    assert 0 == len(result)

    result = n_queens(3)
    assert 0 == len(result)

    result = n_queens(4)
    assert 2 == len(result)

    place1 = [1, 3, 0, 2]
    place2 = [2, 0, 3, 1]
    assert result[0] == place1 or result[0] == place2
    assert result[1] == place1 or result[1] == place2
    assert result[0] != result[1]


def main():
    simple_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 15)
    print('n =', n)
    result = n_queens(n)
    for vec in result:
        text_rep = to_text_representation(vec)
        print(*text_rep, sep='\n')
        print()

if __name__ == '__main__':
    main()
