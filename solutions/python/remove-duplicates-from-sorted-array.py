# remove-duplicates-from-sorted-array.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# @include
def delete_duplicates(A):
    if not A:
        return 0

    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1

    return write_index
# @exclude


def check_ans(A, n):
    for i in range(1, n):
        assert A[i - 1] != A[i]


def small_test():
    A = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    assert delete_duplicates(A) == 6


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(0, 10000)

    for _ in range(1000):
        A = sorted(random.randint(-1000, 1000) for i in range(n))
        B = sorted(set(A))
        size = delete_duplicates(A)
        assert size == len(B)
        check_ans(A, size)
        print(size)


if __name__ == '__main__':
    main()
