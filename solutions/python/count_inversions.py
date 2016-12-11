# Count_inversions.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def count_inversions(A):
    return count_subarray_inversions(0, len(A), A)


# Return the number of inversions in A[start : end - 1].
def count_subarray_inversions(start, end, A):
    if end - start <= 1:
        return 0

    mid = start + ((end - start) // 2)
    return count_subarray_inversions(
        start, mid, A) + count_subarray_inversions(
            mid, end, A) + merge_sort_and_count_inversions_across_subarrays(
                start, mid, end, A)


# Merge two sorted subarrays A[start : mid - 1] and A[mid : end - 1] into A[start : end - 1] and return the number of inversions across A[start : mid - 1] and A[mid : end - 1].
def merge_sort_and_count_inversions_across_subarrays(start, mid, end, A):
    sorted_A = []
    left_start, right_start, inversion_count = start, mid, 0

    while left_start < mid and right_start < end:
        if A[left_start] <= A[right_start]:
            sorted_A.append(A[left_start])
            left_start += 1
        else:
            # A[left_start : mid - 1] are the inversions of A[right_start].
            inversion_count += mid - left_start
            sorted_A.append(A[right_start])
            right_start += 1

    sorted_A += A[left_start:mid]
    sorted_A += A[right_start:end]

    # Updates A with sorted_A.
    A[start:end] = sorted_A
    return inversion_count


# @exclude


# O(n^2) check of inversions.
def n2_check(A):
    count = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                count += 1
    print(count)
    return count


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        A = [random.randint(-1000000, 1000000) for i in range(n)]
        assert n2_check(A) == count_inversions(A)


if __name__ == '__main__':
    main()
