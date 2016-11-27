# String_in_matrix.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def match(A, S):
    cache = set()
    for i in range(len(A)):
        for j in range(len(A[i])):
            if match_helper(A, S, i, j, 0, cache):
                return True
    return False


def match_helper(A, S, i, j, length, cache):
    if len(S) == length:
        return True

    if not 0 <= i < len(A) or not 0 <= j < len(A[i]) or (i, j, length) in cache:
        return False

    if (A[i][j] == S[length] and (
            match_helper(A, S, i - 1, j, length + 1, cache) or
            match_helper(A, S, i + 1, j, length + 1, cache) or
            match_helper(A, S, i, j - 1, length + 1, cache) or
            match_helper(A, S, i, j + 1, length + 1, cache))):
        return True
    cache.add((i, j, length))
    return False
# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(2, 10)
    A = [[random.randrange(n) for j in range(n)] for i in range(n)]
    for a in A:
        print(*a)
    print('S = ', end='')
    S = [random.randrange(n) for i in range(1 + random.randint(1, n * n // 2))]
    print(*S)
    print(match(A, S))


if __name__ == '__main__':
    main()
