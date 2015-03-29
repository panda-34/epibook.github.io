# Max_difference_unlimited_pairs.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def max_profit_unlimited_pairs(A):
    profit = 0
    for i in range(1, len(A)):
        delta = A[i] - A[i - 1]
        if delta > 0:
            profit += delta
    return profit
# @exclude


def check_ans(A):
    profit = 0

    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            profit += A[i] - A[i - 1]
    return profit


def main():
    n = 5
    for _ in range(100):
        A = [random.randint(0, 99) for i in range(n)]
        print('n =', n)
        print(check_ans(A))
        print(max_profit_unlimited_pairs(A))
        assert check_ans(A) == max_profit_unlimited_pairs(A)

    # For input
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10000)
    A = [random.randint(0, 99) for i in range(n)]
    print('n =', n)
    print(max_profit_unlimited_pairs(A))


if __name__ == '__main__':
    main()
