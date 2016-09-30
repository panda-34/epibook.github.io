# nonconstructible-change.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def smallest_nonconstructible_value(A):
    A.sort()
    max_constructible_value = 0
    for a in A:
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a
    return max_constructible_value + 1
# @exclude


def small_test():
    A = [1, 2, 3, 4]
    assert 11 == smallest_nonconstructible_value(A)
    A = [1, 2, 2, 4]
    assert 10 == smallest_nonconstructible_value(A)
    A = [2, 3, 4, 5]
    assert 1 == smallest_nonconstructible_value(A)
    A = [1, 3, 2, 1]
    assert 8 == smallest_nonconstructible_value(A)
    A = [1, 3, 2, 5]
    assert 12 == smallest_nonconstructible_value(A)
    A = [1, 3, 2, 6]
    assert 13 == smallest_nonconstructible_value(A)
    A = [1, 3, 2, 7]
    assert 14 == smallest_nonconstructible_value(A)
    A = [1, 3, 2, 8]
    assert 7 == smallest_nonconstructible_value(A)


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 1000)
    A = [random.randint(1, 1000) for i in range(n)]
    print(*A)
    ans = smallest_nonconstructible_value(A)
    print(ans)


if __name__ == '__main__':
    main()
