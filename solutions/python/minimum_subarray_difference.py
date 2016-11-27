# Minimum_subarray_difference.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def minimize_difference(A):
    sum_ = sum(A)
    is_ok = {0}
    for item in A:
        for v in range(sum_ // 2, item - 1, -1):
            if v - item in is_ok:
                is_ok.add(v)

    # Finds the first i from middle where is_ok[i] == True.
    for i in range(sum_ // 2, 0, -1):
        if i in is_ok:
            return (sum_ - i) - i
    return sum_  # One thief takes all.
# @exclude


def small_test():
    # The example in the book.
    A = (65,  35,  245, 195, 65,  150, 275, 155,
         120, 320, 75,  40,  200, 100, 220, 99)
    assert minimize_difference(A) == 1


def main():
    small_test()
    A = []
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    elif len(sys.argv) == 1:
        n = random.randint(1, 50)
    else:
        for i in sys.argv[1:]:
            A.append(int(i))
        n = 0
    for i in range(n):
        A.append(random.randrange(100))
        print(A[i], end=' ')
    print()
    sum_ = sum(A)
    print(sum_)
    print('difference =', minimize_difference(A))


if __name__ == '__main__':
    main()
