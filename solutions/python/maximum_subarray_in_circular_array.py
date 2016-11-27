# Maximum_subarray_in_circular_array.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def max_subarray_sum_in_circular(A):
    return max(find_max_subarray(A), find_circular_max_subarray(A))


# Calculates the non-circular solution.
def find_max_subarray(A):
    maximum_till = maximum = 0
    for a in A:
        maximum_till = max(a, a + maximum_till)
        maximum = max(maximum, maximum_till)
    return maximum


# Calculates the solution which is circular.
def find_circular_max_subarray(A):
    # Maximum subarray sum starts at index 0 and ends at or before index i.
    sum_ = A[0]
    maximum_begin = [sum_]
    for i in range(1, len(A)):
        sum_ += A[i]
        maximum_begin.append(max(maximum_begin[-1], sum_))

    # Maximum subarray sum starts at index i + 1 and ends at the last element.
    maximum_end = [0] * len(A)
    sum_ = 0
    for i in range(len(A) - 2, -1, -1):
        sum_ += A[i + 1]
        maximum_end[i] = max(maximum_end[i + 1], sum_)

    # Calculates the maximum subarray which is circular.
    circular_max = max(begin + end for begin, end in zip(maximum_begin, maximum_end))
    return circular_max
# @exclude


# O(n^2) solution.
def check_ans(A):
    ans = 0
    for i in range(len(A)):
        sum_ = 0
        for j in range(len(A)):
            sum_ += A[(i + j) % len(A)]
            ans = max(ans, sum_)
    print('correct answer =', ans)
    return ans


def main():
    for times in range(1000):
        if len(sys.argv) > 2:
            A = [int(i) for i in sys.argv[1:]]
        else:
            if len(sys.argv) == 2:
                n = int(sys.argv[1])
            else:
                n = random.randint(1, 10000)
            A = [random.randint(-10000, 10000) for i in range(n)]
        ans = max_subarray_sum_in_circular(A)
        print('\nmaximum sum =', ans)
        assert ans == check_ans(A)


if __name__ == '__main__':
    main()
