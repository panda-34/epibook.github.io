# Rotate_array.h 848813e190b1b85a8e75107fe8513c3be38ad1a9
# Rotate_array.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import rotate_array_permutation


# @include
def rotate_array(i, A):
    i %= len(A)
    A[:] = A[::-1]  # reverse whole list
    A[:i] = A[:i][::-1]  # reverse [:i] part
    A[i:] = A[i:][::-1]  # reverse [i:] part


# @exclude


def check_answer(A, i, rotated):
    assert len(A) == len(rotated)
    assert all(rotated[(idx + i) % len(rotated)] == A[idx]
               for idx in range(len(A)))


def main():
    for _ in range(1000):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1,
                                                                       10000)
        A = [random.randint(0, n) for _ in range(n)]
        i = random.randrange(n)
        B = A.copy()
        rotate_array(i, B)
        check_answer(A, i, B)
        C = A.copy()
        rotate_array_permutation.rotate_array(i, C)
        check_answer(A, i, C)


if __name__ == '__main__':
    main()
