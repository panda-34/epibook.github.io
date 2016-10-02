# permutations-alternative.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def permutations(A):
    result = []
    directed_permutations(0, A, result)
    return result


def directed_permutations(i, A, result):
    if i == len(A) - 1:
        result.append(A.copy())
        return

    # Try every possibility for A[i].
    for j in range(i, len(A)):
        A[i], A[j] = A[j], A[i]
        # Generate all permutations for A[i + 1 : len(A) - 1].
        directed_permutations(i + 1, A, result)
        A[i], A[j] = A[j], A[i]
# @exclude


def small_test():
    A = [0, 1, 2]
    result = permutations(A)
    golden_result = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
    assert result == golden_result


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10)
    A = list(range(n))
    result = permutations(A)
    print('n =', n)
    for vec in result:
        print(*vec)


if __name__ == '__main__':
    main()
