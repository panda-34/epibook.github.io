# rook-attack.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import copy


# @include
def rook_attack(A):
    m = len(A)
    n = len(A[0])
    has_first_row_zero = False
    for j in range(n):
        if not A[0][j]:
            has_first_row_zero = True
            break
    has_first_column_zero = False
    for i in range(m):
        if not A[i][0]:
            has_first_column_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if not A[i][j]:
                A[i][0] = A[0][j] = 0

    for i in range(1, m):
        if not A[i][0]:
            for j in range(1, n):
                A[i][j] = 0

    for j in range(1, n):
        if not A[0][j]:
            for i in range(1, m):
                A[i][j] = 0

    if has_first_row_zero:
        for j in range(n):
            A[0][j] = 0

    if has_first_column_zero:
        for i in range(m):
            A[i][0] = 0
# @exclude


def check_ans(A, ans):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if not A[i][j]:
                for k in range(len(ans)):
                    assert not ans[k][j]
                for k in range(len(ans[i])):
                    assert not ans[i][k]


def main():
    for _ in range(1000):
        if len(sys.argv) == 3:
            m = int(sys.argv[1])
            n = int(sys.argv[2])
        else:
            m = random.randint(1, 50)
            n = random.randint(1, 50)
        A = []
        for i in range(m):
            A.append([random.randint(0, 1) for j in range(n)])
        copy_A = copy.deepcopy(A)
        print('m = %d, n = %d' % (m, n))
        rook_attack(A)
        check_ans(copy_A, A)


if __name__ == '__main__':
    main()
