# Painting_recursive.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def flip_color(x, y, A):
    color = A[x][y]
    A[x][y] = 1 - A[x][y]  # Flips.
    for d in (0, 1), (0, -1), (1, 0), (-1, 0):
        next_x, next_y = x + d[0], y + d[1]
        if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and
                A[next_x][next_y] == color):
            flip_color(next_x, next_y, A)


# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 100)

    A = []
    for i in range(n):
        A.append([random.randint(0, 1) for j in range(n)])

    i = random.randrange(n)
    j = random.randrange(n)
    print('color =', i, j, A[i][j])
    print(*A)
    flip_color(i, j, A)
    print()
    print(*A)


if __name__ == '__main__':
    main()
