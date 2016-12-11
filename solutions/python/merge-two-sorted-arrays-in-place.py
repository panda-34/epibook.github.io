# merge-two-sorted-arrays-in-place.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def merge_two_sorted_arrays(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx -= 1
        b -= 1
# @exclude


def check_ans(A):
    assert all(A[i - 1] <= A[i] for i in range(1, len(A)))


def main():
    for _ in range(1000):
        if len(sys.argv) == 3:
            m = int(sys.argv[1])
            n = int(sys.argv[2])
        else:
            m = random.randint(0, 10000)
            n = random.randint(0, 10000)
        A = sorted(random.randint(-(m + n), m + n) for i in range(m)) + [None] * n
        B = sorted(random.randint(-(m + n), m + n) for i in range(n))
        merge_two_sorted_arrays(A, m, B, n)
        check_ans(A)


if __name__ == '__main__':
    main()
