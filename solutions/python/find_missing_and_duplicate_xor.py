# Find_missing_and_duplicate_XOR.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def find_duplicate_missing(A):
    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A.
    miss_XOR_dup = 0
    for i, a in enumerate(A):
        miss_XOR_dup ^= i ^ a

    # We need to find a bit that's set to 1 in miss_XOR_dup. Such a bit
    # must exist if there is a single missing number and a single duplicated
    # number in A.
    #
    # The bit-fiddling assignment below sets all of bits in differ_bit to 0
    # except for the least significant bit in miss_XOR_dup that's 1.
    differ_bit = miss_XOR_dup & (~(miss_XOR_dup - 1))
    miss_or_dup = 0
    for i, a in enumerate(A):
        # Focus on entries and numbers in which the differ_bit-th bit is 1.
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    # miss_or_dup is either the missing value or the duplicated entry.
    for A_i in A:
        if A_i == miss_or_dup:  # miss_or_dup is the duplicate.
            return miss_or_dup, miss_or_dup ^ miss_XOR_dup
    # miss_or_dup is the missing value.
    return miss_or_dup ^ miss_XOR_dup, miss_or_dup
# @exclude


def simple_test():
    A = [0, 1, 2, 4, 5, 6, 6]
    ans = find_duplicate_missing(A)
    assert ans[0] == 6 and ans[1] == 3

    A = [0, 0, 1]
    ans = find_duplicate_missing(A)
    assert ans[0] == 0 and ans[1] == 2

    A = [1, 3, 2, 5, 3, 4]
    ans = find_duplicate_missing(A)
    assert ans[0] == 3 and ans[1] == 0


def main():
    simple_test()
    for times in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(2, 10000)
        A = list(range(n))
        missing_idx = random.randrange(n)
        missing = A[missing_idx]
        dup_idx = random.randrange(n)
        while dup_idx == missing_idx:
            dup_idx = random.randrange(n)
        dup = A[dup_idx]
        A[missing_idx] = dup
        ans = find_duplicate_missing(A)
        print('times =', times)
        print(dup, missing)
        print(ans[0], ans[1])
        assert ans[0] == dup and ans[1] == missing


if __name__ == '__main__':
    main()
