# Longest_increasing_subarray.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def find_longest_increasing_subarray(A):
    max_length = 1
    ans = (0, 0)
    i = 0
    while i < len(A) - max_length:
        # Backward check and skip if A[j] >= A[j + 1].
        for j in range(i + max_length, i, -1):
            if A[j - 1] >= A[j]:
                i = j
                break
        else:  # Forward check if it is not skippable (the loop ended normally)
            max_length += 1
            i += max_length
            while i < len(A) and A[i - 1] < A[i]:
                max_length += 1
                i += 1
            ans = (i - max_length, i - 1)
    return ans
# @exclude


def simple_test():
    ans = find_longest_increasing_subarray([-1, -1])
    assert ans == (0, 0)
    ans = find_longest_increasing_subarray([1, 2])
    assert ans == (0, 1)


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) > 2:
            A = list(map(int, sys.argv[1:]))
        else:
            if len(sys.argv) == 2:
                n = int(sys.argv[1])
            else:
                n = random.randint(1, 1000000)
            A = [random.randint(-(n - 1), n - 1) for i in range(n)]
        result = find_longest_increasing_subarray(A)
        print(*result)
        max_len = 1
        cur_len = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
        assert max_len == result[1] - result[0] + 1


if __name__ == '__main__':
    main()
