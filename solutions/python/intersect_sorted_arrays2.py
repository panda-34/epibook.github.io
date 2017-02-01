# Intersect_sorted_arrays2.h 4a4c5f91493e5e482eaa79892816c1ccefa084f4
import bisect


# @include
def intersect_two_sorted_arrays(A, B):
    def is_present(A, k):
        i = bisect.bisect_left(A, k)
        return i < len(A) and A[i] == k

    intersection_A_B = []
    for i in range(len(A)):
        if (i == 0 or A[i] != A[i - 1]) and is_present(B, A[i]):
            intersection_A_B.append(A[i])
    return intersection_A_B


# @exclude
