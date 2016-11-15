# sort_k-increasing-decreasing_array.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import itertools
from merge_sorted_arrays import merge_sorted_arrays


# @include
def sort_k_increasing_decreasing_array(A):
    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type = INCREASING
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or  # A is ended. Adds the last subarray.
            (A[i - 1] < A[i] and subarray_type == DECREASING) or
            (A[i - 1] >= A[i] and subarray_type == INCREASING)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type ==
                                    INCREASING else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = DECREASING if subarray_type == INCREASING else INCREASING
    return merge_sorted_arrays(sorted_subarrays)


# @exclude


class Monotonic:
    def __init__(self):
        self.last = float('-inf')

    def __call__(self, curr):
        res = curr < self.last
        self.last = curr
        return res


def sort_k_increasing_decreasing_array_pythonic(A):
    return merge_sorted_arrays([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
    ])


# @exclude


def simple_test():
    A = [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
    assert sorted(A) == sort_k_increasing_decreasing_array(
        A) == sort_k_increasing_decreasing_array_pythonic(A)

    A = [-2**64, -1, 0, 1, 2, 4, 8, 2**64 - 1]
    assert sorted(A) == sort_k_increasing_decreasing_array(
        A) == sort_k_increasing_decreasing_array_pythonic(A)

    A = list(reversed(A))
    assert sorted(A) == sort_k_increasing_decreasing_array(
        A) == sort_k_increasing_decreasing_array_pythonic(A)


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        print('n =', n)
        A = [random.randint(-999999, 999999) for i in range(n)]
        ans = sort_k_increasing_decreasing_array(A)
        #        print(*A)
        #        print(*ans)
        assert len(ans) == len(A)
        assert ans == sorted(ans)
        assert ans == sort_k_increasing_decreasing_array_pythonic(A)


if __name__ == '__main__':
    main()
