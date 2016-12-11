# combinations.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def combinations(n, k):
    result = []
    directed_combinations(n, k, 1, [], result)
    return result


def directed_combinations(n, k, offset, partial_combination, result):
    if len(partial_combination) == k:
        result.append(list(partial_combination))
        return

    # Generate remaining combinations over {offset, ..., n - 1} of size
    # num_remaining.
    num_remaining = k - len(partial_combination)
    i = offset
    while i <= n and num_remaining <= n - i + 1:
        partial_combination.append(i)
        directed_combinations(n, k, i + 1, partial_combination, result)
        del partial_combination[-1]
        i += 1


# @exclude


def small_test():
    assert combinations(4,
                        2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]


def main():
    small_test()
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        n = random.randint(1, 10)
        k = random.randint(0, n)
    result = combinations(n, k)
    print('n = ', n, ', k = ', k, sep='')
    for vec in result:
        print(*vec)


if __name__ == '__main__':
    main()
