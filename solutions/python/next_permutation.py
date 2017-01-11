# Next_permutation.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import math
import collections
import functools
import operator


# @include
def next_permutation(p):
    k = len(p) - 2
    while k >= 0 and p[k] >= p[k + 1]:
        k -= 1
    if k == -1:
        return False  # p is the last permutation.

    # Swap the smallest entry after index k that is greater than p[k].
    # We exploit the fact that p[k + 1 : ] is decreasing so if we
    # search in reverse order, the first entry that is greater than p[k] is
    # the smallest such entry.
    for i in range(len(p) - 1, k, -1):
        if p[i] > p[k]:
            p[k], p[i] = p[i], p[k]
            break

    # Since p[k + 1 : ] is in decreasing order, we can build the
    # smallest dictionary ordering of this subarray by reversing it.
    p[k + 1:] = p[len(p) - 1:k:-1]
    return True


# @exclude


def main():
    if len(sys.argv) > 2:
        p = list(map(int, sys.argv[1:]))
        if next_permutation(p):
            print(*p)
        else:
            print('This is the last permutation')
    else:
        for _ in range(1000):
            n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1,
                                                                           15)
            p = sorted(random.randrange(n)
                       for i in range(n))  # first permutation
            p_last = sorted(p, reverse=True)  # last permutation
            ms = collections.Counter(p)  # elements' multiplicities
            # multinomial coefficient = n! / (m1! * m2! * ...)
            multinom = math.factorial(n) // functools.reduce(
                operator.mul, map(math.factorial, ms.values()))
            if multinom > 100000000:
                continue
            print('n:', n, 'permutations:', multinom)
            count = 1
            while next_permutation(p):
                count += 1
            assert p == p_last
            assert count == multinom


if __name__ == '__main__':
    main()
