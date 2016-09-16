# Finding_min_max.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def find_min_max(A):
    if len(A) <= 1:
        return A[0], A.front()[0]

    global_min_max = min(A[:2]), max(A[:2])
    # Process two elements at a time.
    for i in range(2, len(A)-1, 2):
        local_min_max = min(A[i:i+2]), max(A[i:i+2])
        global_min_max = (min(global_min_max[0], local_min_max[0]),
                          max(global_min_max[1], local_min_max[1]))
    # If there is odd number of elements in the array, still
    # need to compare the last element with the existing answer.
    if len(A) % 2:
        global_min_max = (min(global_min_max[0], A[-1]),
                          max(global_min_max[1], A[-1]))
    return global_min_max
# @exclude


def simple_test():
    A = [-1, 3, -4, 6, 4, 10, 4, 4, 9]
    res = find_min_max(A)
    assert res == (-4, 10)
    A[5] = -12
    res = find_min_max(A)
    assert res == (-12, 9)
    A = [-1, 3, -4]
    res = find_min_max(A)
    assert res == (-4, 3)


def main():
    simple_test()
    for _ in range(10000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        A = [random.randrange(1000000) for i in range(n)]
        res = find_min_max(A)
        assert res == (min(A), max(A))


if __name__ == '__main__':
    main()
