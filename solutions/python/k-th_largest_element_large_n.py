# k-th_largest_element_large_n.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import operator
import random
import heapq


# @include
def find_kth_largest_unknown_length(sin, k):
    candidates = []
    for x in sin:
        candidates.append(x)
        if len(candidates) >= 2 * k - 1:
            # Reorders elements about median with larger elements appearing before
            # the median.
            nth_element(candidates, k - 1, operator.gt)
            # Resize to keep just the k largest elements seen so far.
            del candidates[k:]
    # Finds the k-th largest element in candidates.
    nth_element(candidates, k - 1, operator.gt)
    return candidates[k - 1]


# @exclude


def nth_element(seq, n, compare=operator.lt, left=0, right=None):
    if right is None:
        right = len(seq) - 1
    if left >= right:
        return

    pivot = random.randint(left, right)
    pivot_value = seq[pivot]
    seq[pivot], seq[right] = seq[right], pivot_value

    pivot = left
    for i in range(left, right):
        if compare(seq[i], pivot_value):
            seq[pivot], seq[i] = seq[i], seq[pivot]
            pivot += 1
    seq[pivot], seq[right] = seq[right], seq[pivot]

    if n == pivot:
        return
    if n < pivot:
        nth_element(seq, n, compare, left, pivot - 1)
    else:
        nth_element(seq, n, compare, pivot + 1, right)


def find_kth_largest_unknown_length_pythonic(sin, k):
    return heapq.nlargest(k, sin)[-1]


def simple_test_array(A):
    A_sorted = sorted(A, reverse=True)
    for i in range(len(A)):
        print('i =', i)
        k = i + 1
        result = find_kth_largest_unknown_length(iter(A), k)
        assert result == A_sorted[k - 1]
        assert result == find_kth_largest_unknown_length_pythonic(iter(A), k)


def simple_test():
    A = [5, 6, 2, 1, 3, 0, 4]
    simple_test_array(A)
    A = [5, -1, 2, 1, 3, 1, 4, 2 << 31 - 1, 5]
    simple_test_array(A)
    N = 1000
    A = [random.randrange(10) for i in range(N)]
    simple_test_array(A)
    A = [random.randrange(100000000) for i in range(N)]
    simple_test_array(A)


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
            k = random.randint(1, n)
        elif len(sys.argv) == 3:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
        else:
            n = random.randint(1, 100000)
            k = random.randint(1, n)
        A = [random.randrange(10000000) for i in range(n)]
        result = find_kth_largest_unknown_length(iter(A), k)
        result_pythonic = find_kth_largest_unknown_length_pythonic(iter(A), k)
        A.sort(reverse=True)
        print(result, A[k - 1])
        assert result == A[k - 1]
        assert result == result_pythonic


if __name__ == '__main__':
    main()
