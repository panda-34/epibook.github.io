# Find_missing_and_duplicate.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def find_duplicate_missing(A):
    sum = square_sum = 0
    for i, a in enumerate(A):
        sum += i - a
        square_sum += i ** 2 - a ** 2
    return (square_sum // sum - sum) // 2, (square_sum // sum + sum) // 2
# @exclude


def main():
    for times in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(2, 10000)
        A = list(range(n))
        missing_idx = random.randrange(n)
        missing = A[missing_idx]
        dup_idx = random.randrange(n)
        while dup_idx == missing_idx:
            dup_idx = random.randrange(n)
        dup = A[dup_idx]
        A[missing_idx] = dup
        ans = find_duplicate_missing(A)
        print('times =', times)
        print(dup, missing)
        print(ans[0], ans[1])
        assert ans[0] == dup and ans[1] == missing


if __name__ == '__main__':
    main()
