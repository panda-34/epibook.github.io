# Painting_iterative.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import collections


# @include
def filp_color(x, y, A):
    color = A[x][y]

    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
    q = collections.deque()
    A[x][y] = 1 - A[x][y]  # Flips.
    q.append(Coordinate(x, y))
    while q:
        curr = q.popleft()
        for d in (0, 1), (0, -1), (1, 0), (-1, 0):
            next_x, next_y = curr.x + d[0], curr.y + d[1]
            if (0 <= next_x < len(A) and 0 <= next_y < len(A[next_x]) and
                    A[next_x][next_y] == color):
                # Flips the color.
                A[next_x][next_y] = 1 - A[next_x][next_y]
                q.append(Coordinate(next_x, next_y))


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
    filp_color(i, j, A)
    print()
    print(*A)


if __name__ == '__main__':
    main()
