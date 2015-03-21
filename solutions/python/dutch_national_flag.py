# Dutch_national_flag.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    # Keep the following invariants during partitioning:
    # bottom group: A[ : smaller].
    # middle group: A[smaller : equal].
    # unclassified group: A[equal : larger + 1].
    # top group: A[larger + 1 : ].
    smaller = 0
    equal = 0
    larger = len(A) - 1
    # When there is any unclassified element.
    while equal <= larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            A[equal], A[larger] = A[larger], A[equal]
            larger -= 1
# @exclude


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 100)
        A = [random.randint(0, 2) for i in range(n)]
        pivot_index = random.randrange(n)
        pivot = A[pivot_index]
        dutch_flag_partition(pivot_index, A)
        i = 0
        while i < len(A) and A[i] < pivot:
            print(A[i], end=' ')
            i += 1
        while i < len(A) and A[i] == pivot:
            print(A[i], end=' ')
            i += 1
        while i < len(A) and A[i] > pivot:
            print(A[i], end=' ')
            i += 1
        print()
        assert i == len(A)


if __name__ == '__main__':
    main()
