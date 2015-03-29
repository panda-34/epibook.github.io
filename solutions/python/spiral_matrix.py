# Spiral_matrix.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import itertools


# @include
def print_matrix_in_spiral_order(A):
    shift = ((0, 1), (1, 0),
             (0, -1), (-1, 0))
    d = x = y = 0

    for i in range(len(A) ** 2):
        print(A[x][y], end=' ')
        A[x][y] = 0
        next_x = x + shift[d][0]
        next_y = y + shift[d][1]
        if (next_x not in range(len(A)) or next_y not in range(len(A))
                or A[next_x][next_y] == 0):
            d = (d + 1) & 3
            next_x = x + shift[d][0]
            next_y = y + shift[d][1]
        x = next_x
        y = next_y
# @exclude


def print_matrix_in_spiral_order2(A):
    shift = (1, 1, -1, -1)  # step size for each direction
    limits = [len(A)-1, len(A)-1, 0, 1]  # need to change direction at this point
    xy = [0, 0]  # x and y coordinates
    x_or_y = 1  # which coordinate changes now
    d = 0

    for i in range(len(A) ** 2):
        print(A[xy[0]][xy[1]], end=' ')
        if xy[x_or_y] == limits[d]:  # at the last point in this direction
            limits[d] -= shift[d]  # one row/column less next time
            d = (d + 1) & 3
            x_or_y = 1 - x_or_y  # change other coordinate from now on
        xy[x_or_y] += shift[d]


def main():
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        N = random.randint(1, 50)
    k = itertools.count(1)
    A = []
    for i in range(N):
        A.append([next(k) for j in range(N)])
    print_matrix_in_spiral_order2(A)
    print()
    print_matrix_in_spiral_order(A)


if __name__ == '__main__':
    main()
