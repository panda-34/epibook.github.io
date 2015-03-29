# Biggest_product_n-1.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import itertools
import operator


# @include
def find_biggest_n_minus_one_product(A):
    # Builds forward product L, backward product R.
    L = list(itertools.accumulate(A, operator.mul))
    R = list(itertools.accumulate(reversed(A), operator.mul))
    R.reverse()

    # Finds the biggest product of (n - 1) numbers.
    max_product = float('-inf')
    for i in range(len(A)):
        forward = L[i - 1] if i > 0 else 1
        backward = R[i + 1] if i + 1 < len(A) else 1
        max_product = max(max_product, forward * backward)
    return max_product
# @exclude


# n^2 checking.
def check_ans(A):
    max_product = float('-inf')
    for i in range(len(A)):
        product = 1
        for j in range(i):
            product *= A[j]
        for j in range(i + 1, len(A)):
            product *= A[j]
        if product > max_product:
            max_product = product
    return max_product


def main():
    for _ in range(10000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(2, 11)
        A = [random.randint(-9, 9) for i in range(n)]
        print(*A)
        res = find_biggest_n_minus_one_product(A)
        assert res == check_ans(A)
        print(res)


if __name__ == '__main__':
    main()
