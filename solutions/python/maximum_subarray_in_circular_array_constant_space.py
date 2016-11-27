# Maximum_subarray_in_circular_array_constant_space.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def max_subarray_sum_in_circular(A):
    # Finds the max in non-circular case and circular case.
    return max(find_optimum_subarray_using_comp(A, max),  # Non-circular case.
               sum(A) - find_optimum_subarray_using_comp(A, min))  # Circular case.

def find_optimum_subarray_using_comp(A, comp):
    till = overall = 0
    for a in A:
        till = comp(a, a + till)
        overall = comp(overall, till)
    return overall
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
