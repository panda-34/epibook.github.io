# Max_submatrix_square.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import collections


# O(m^3 n^3) time solution.
def check_ans(A):
    max = 0
    for a in range(len(A)):
        for b in range(len(A[a])):
            r = 1
            while a + r <= len(A) and b + r <= len(A[0]):
                count = 0
                all_1 = True
                for c in range(a, a + r):
                    for d in range(b, b + r):
                        if A[c][d]:
                            count += 1
                        else:
                            all_1 = False
                            count = 0
                            break
                    if all_1 == False:
                        break
                if count > max:
                    max = count
                r += 1
    return max


# @include


def max_square_submatrix(A):
    MaxHW = collections.namedtuple('MaxHW', ('h', 'w'))
    # DP table stores (h, w) for each (i, j).
    table = [[None] * len(A[0]) for i in A]

    for i in range(len(A) - 1, -1, -1):
        for j in range(len(A[i]) - 1, -1, -1):
            # Finds the largest h such that (i, j) to (i + h - 1, j) are feasible.
            # Finds the largest w such that (i, j) to (i, j + w - 1) are feasible.
            table[i][j] = (MaxHW(table[i + 1][j].h + 1 if i + 1 < len(A) else
                                 1, table[i][j + 1].w + 1
                                 if j + 1 < len(A[i]) else 1)
                           if A[i][j] else MaxHW(0, 0))

    # A table stores the length of the largest square for each (i, j).
    s = [[0] * len(A[0]) for i in A]
    max_square_area = 0
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(A[i]) - 1, -1, -1):
            if A[i][j]:
                side = min(table[i][j].h, table[i][j].w)
                # Gets the length of largest square with bottom-left corner (i, j).
                if i + 1 < len(A) and j + 1 < len(A[i + 1]):
                    side = min(s[i + 1][j + 1] + 1, side)
                s[i][j] = side
                max_square_area = max(max_square_area, side**2)
    return max_square_area


# @exclude


def main():
    for times in range(1000):
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        else:
            n = random.randint(1, 50)
            m = random.randint(1, 50)
        A = [[bool(random.randrange(2)) for j in range(m)] for i in range(n)]
        for i in range(n):
            print(*map(int, A[i]))
        print(max_square_submatrix(A))
        print(check_ans(A))
        assert check_ans(A) == max_square_submatrix(A)


if __name__ == '__main__':
    main()
