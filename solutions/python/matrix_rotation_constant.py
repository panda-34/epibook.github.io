# Matrix_rotation_constant.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import itertools
import copy


def rotate_matrix(A):
    for i in range(len(A) // 2):
        for j in range(i, len(A) - i - 1):
            temp = A[i][j]
            A[i][j] = A[-1 - j][i]
            A[-1 - j][i] = A[-1 - i][-1 - j]
            A[-1 - i][-1 - j] = A[j][-1 - i]
            A[j][-1 - i] = temp


# @include
class RotatedMatrix:
    def __init__(self, square_matrix):
        self.__square_matrix = copy.deepcopy(square_matrix)

    def read_entry(self, i, j):
        return self.__square_matrix[-1 - j][i]

    def write_entry(self, i, j, v):
        self.__square_matrix[-1 - j][i] = v
# @exclude


def check_answer(A, B):
    rA = RotatedMatrix(A)
    for i in range(len(A)):
        for j in range(len(A)):
            assert rA.read_entry(i, j) == B[i][j]


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = itertools.count(1)
        A = []
        for i in range(1 << n):
            A.append([next(k) for j in range(1 << n)])
        B = copy.deepcopy(A)
        rotate_matrix(B)
        check_answer(A, B)
    else:
        for _ in range(100):
            n = random.randint(1, 10)
            k = itertools.count(1)
            A = []
            for i in range(1 << n):
                A.append([next(k) for j in range(1 << n)])
            B = copy.deepcopy(A)
            rotate_matrix(B)
            check_answer(A, B)


if __name__ == '__main__':
    main()
