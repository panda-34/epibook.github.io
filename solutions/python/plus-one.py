# plus-one.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def plus_one(A):
    A[-1] += 1
    for i in range(len(A) - 1, 0, -1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        # Need additional digit as the most significant digit (i.e., A[0]) has a carry-out.
        A[0] = 0
        A.insert(0, 1)
    return A
# @exclude


def rand_vector(length):
    if not length:
        return [0]
    A = [random.randint(1, 9)]
    A += [random.randint(0, 9) for i in range(length - 1)]
    return A


def small_test():
    result = plus_one([9, 9])
    assert result == [1, 0, 0]
    result = plus_one([3, 1, 4])
    assert result == [3, 1, 5]


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(0, 1000)
    A = rand_vector(n)
    print(*A, sep='')
    result = plus_one(A)
    print(*result, sep='')
    print()


if __name__ == '__main__':
    main()
