# first-missing-positive.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


def check_ans(A):
    A = sorted(A)
    target = 1
    for a in A:
        if a > 0:
            if a == target:
                target += 1
            elif a > target:
                return target
    return target


# @include
def find_first_missing_positive(A):
    # Record which values are present by writing A[i] to index A[i] - 1 if A[i]
    # is between 1 and len(A), inclusive. We save the value at index
    # A[i] - 1 by swapping it with the entry at i. If A[i] is negative or
    # greater than n, we just advance i.
    A = A.copy()
    i = 0
    while i < len(A):
        if A[i] > 0 and A[i] <= len(A) and A[A[i] - 1] != A[i]:
            tmp = A[i]
            A[i] = A[tmp-1]
            A[tmp-1] = tmp
        else:
            i += 1

    # Second pass through A to search for the first index i such that
    # A[i] != i+1, indicating that i + 1 is absent. If all numbers between 1
    # and len(A) are present, the smallest missing positive is len(A) + 1.
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    return len(A) + 1
# @exclude


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(0, 500000)

        A = [random.randint(0, n) for i in range(n)]
        print('n =', n)
        #print(*A)
        #print(find_first_missing_positive(A), check_ans(A))
        assert find_first_missing_positive(A) == check_ans(A)


if __name__ == '__main__':
    main()
 