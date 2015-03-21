# remove-duplicates-from-sorted-array.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# @include
def remove_duplicates(A):
    if not A:
        return 0

    write_index = 0
    for i in range(1, len(A)):
        if A[write_index] != A[i]:
            write_index += 1
            A[write_index] = A[i]

    return write_index + 1
# @exclude


def check_ans(A, n):
    for i in range(1, n):
        assert A[i - 1] != A[i]


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(0, 10000)

    for _ in range(1000):
        A = sorted(random.randint(-1000, 1000) for i in range(n))
        B = sorted(set(A))
        size = remove_duplicates(A)
        assert size == len(B)
        check_ans(A, size)
        print(size)


if __name__ == '__main__':
    main()
