# Binary_search_first_k.cpp 69dab7578339012270872ba200cfff02f59ce894
import sys
import random
import bisect


# @include
def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    # [left : right] is the candidate set.
    while left <= right:
        mid = left + ((right - left) // 2)
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution.
        else:  # A[mid] < k.
            left = mid + 1
    return result


# @exclude


def simple_test():
    A = [0, 1, 2, 3, 4, 5, 6, 7]
    assert 0 == search_first_of_k(A, 0)
    assert 1 == search_first_of_k(A, 1)
    assert 4 == search_first_of_k(A, 4)
    assert 6 == search_first_of_k(A, 6)
    assert 7 == search_first_of_k(A, 7)
    assert -1 == search_first_of_k(A, 8)
    assert -1 == search_first_of_k(A, -2**64)
    A[0] = 1
    assert 0 == search_first_of_k(A, 1)
    A[5] = 4
    A[6] = 4
    assert 4 == search_first_of_k(A, 4)
    A = [1, 1, 1, 1, 1, 2]
    assert -1 == search_first_of_k(A, 0)
    assert 0 == search_first_of_k(A, 1)
    assert 5 == search_first_of_k(A, 2)
    A[4] = 2
    assert 4 == search_first_of_k(A, 2)


# Pythonic solution
def search_first_of_k_pythonic(A, k):
    i = bisect.bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 100000)
        k = random.randrange(n)
        A = sorted(random.randrange(n) for i in range(n))
        ans = search_first_of_k(A, k)
        print('k =', k, 'locates at', ans)
        if ans != -1:
            print('A[k] =', A[ans])
        try:
            it = A.index(k)
        except ValueError:
            it = -1
        assert it == ans
        assert it == search_first_of_k_pythonic(A, k)


if __name__ == '__main__':
    main()
