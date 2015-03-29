# Spiral_matrix_clockwise.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import itertools


# @include
def print_matrix_in_spiral_order(A):
    for offset in range((len(A) + 1) // 2):
        print_matrix_clockwise(A, offset)


def print_matrix_clockwise(A, offset):
    if offset == len(A) - offset - 1:
        # A has odd dimension, and we are at the center of the matrix A.
        print(A[offset][offset])
        return
    for j in range(offset, len(A) - offset - 1):
        print(A[offset][j], end=' ')
    for i in range(offset, len(A) - offset - 1):
        print(A[i][-1 - offset], end=' ')
    for j in range(len(A) - offset - 1, offset, -1):
        print(A[-1 - offset][j], end=' ')
    for i in range(len(A) - offset - 1, offset, -1):
        print(A[i][offset], end=' ')
# @exclude


def main():
    if len(sys.argv) == 2:
        N = int(sys.argv[1])
    else:
        N = random.randint(1, 50)
    k = itertools.count(1)
    A = []
    for i in range(N):
        A.append([next(k) for j in range(N)])
    print_matrix_in_spiral_order(A)


if __name__ == '__main__':
    main()
