# Longest_subarray_k_improved.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import itertools


# @include
def find_longest_subarray_less_equal_k(A, k):
    # Builds the prefix sum according to A.
    prefix_sum = list(itertools.accumulate(A))

    # Early returns if the sum of A is smaller than or equal to k.
    if prefix_sum[-1] <= k:
        return len(A)

    # Builds min_prefix_sum.
    min_prefix_sum = [None] * len(A)
    min_prefix_sum[-1] = prefix_sum[-1]
    for i in range(len(min_prefix_sum) - 2, -1, -1):
        min_prefix_sum[i] = min(prefix_sum[i], min_prefix_sum[i + 1])

    a = b = max_length = 0
    while a < len(A) and b < len(A):
        min_curr_sum = min_prefix_sum[b] - prefix_sum[a - 1] if a > 0 else min_prefix_sum[b]
        if min_curr_sum <= k:
            curr_length = b - a + 1
            if curr_length > max_length:
                max_length = curr_length
            b += 1
        else:  # min_curr_sum > k.
            a += 1
    return max_length
# @exclude


# O(n^2) checking answer.
def check_answer(A, ans, k):
    sum_ = [0]
    sum_.extend(itertools.accumulate(A))
    if ans != 0:
        for i in range(len(sum_)):
            for j in range(i + 1, len(sum_)):
                if sum_[j] - sum_[i] <= k:
                    assert (j - i) <= ans
    else:
        for i in range(len(sum_)):
            for j in range(i + 1, len(sum_)):
                assert sum_[j] - sum_[i] > k


def small_test():
    A = (1, 1)
    k = 0
    res = find_longest_subarray_less_equal_k(A, k)
    assert res == 0
    k = -100
    res = find_longest_subarray_less_equal_k(A, k)
    assert res == 0


def main():
    small_test()
    for times in range(1000):
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
        elif len(sys.argv) == 2:
            n = int(sys.argv[1])
            k = random.randint(0, 9999)
        else:
            n = random.randint(1, 10000)
            k = random.randint(0, 9999)
        A = [random.randint(-1000, 1000) for i in range(n)]
        ans = find_longest_subarray_less_equal_k(A, k)
        print(k, ans)
        check_answer(A, ans, k)


if __name__ == '__main__':
    main()
