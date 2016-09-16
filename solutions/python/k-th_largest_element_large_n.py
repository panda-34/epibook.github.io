# k-th_largest_element_large_n.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import heapq


# @include
def find_kth_largest_unknown_length(sin, k):
    return heapq.nlargest(k, sin)[-1]
# @exclude


def simple_test_array(A):
    A_sorted = sorted(A, reverse=True)
    for i in range(len(A)):
        print('i =', i)
        k = i + 1
        result = find_kth_largest_unknown_length(A, k)
        assert result == A_sorted[k-1]


def simple_test():
    A = [5, 6, 2, 1, 3, 0, 4]
    simple_test_array(A)
    A = [5, -1, 2, 1, 3, 1, 4, 2 << 31 - 1, 5]
    simple_test_array(A);
    N = 1000
    A = [random.randrange(10) for i in range(N)]
    simple_test_array(A)
    A = [random.randrange(100000000) for i in range(N)]
    simple_test_array(A)


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
            k = random.randint(1, n)
        elif len(sys.argv) == 3:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
        else:
            n = random.randint(1, 100000)
            k = random.randint(1, n)
        A = [random.randrange(10000000) for i in range(n)]
        result = find_kth_largest_unknown_length(A, k)
        A.sort(reverse=True)
        print(result, A[k-1])
        assert result == A[k-1]


if __name__ == '__main__':
    main()
