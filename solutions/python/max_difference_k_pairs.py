# Max_difference_k_pairs.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def max_k_pairs_profits(A, k):
    k_sum = [float('-inf')] * (2 * k)
    for i in range(len(A)):
        pre_k_sum = k_sum.copy()
        sign = -1
        for j in range(min(len(k_sum), i+1)):
            diff = sign * A[i] + (0 if j == 0 else pre_k_sum[j - 1])
            k_sum[j] = max(diff, pre_k_sum[j])
            sign *= -1
    return k_sum[-1]  # Returns the last selling profits as the answer.
# @exclude


# O(n^k) checking answer.
def check_ans_helper(A, l, k, pre, ans, max_ans):
    if l == k:
        return max(max_ans, ans)
    else:
        for i in range(pre, len(A)):
            max_ans = check_ans_helper(
                A, l + 1, k, i + 1, ans + (A[i] if l & 1 else -A[i]), max_ans)
        return max_ans


def check_ans(A, k):
    ans = 0
    max_ans = float('-inf')

    max_ans = check_ans_helper(A, 0, 2 * k, 0, ans, max_ans)
    print('max_ans =', max_ans)
    return max_ans


def main():
    n = 40
    k = 4
    # random tests n = 40, k = 4 for 100 times
    for _ in range(100):
        A = [random.randint(0, 99) for i in range(n)]
        print('n = %d, k = %d' % (n, k))
        print(max_k_pairs_profits(A, k))
        assert check_ans(A, k) == max_k_pairs_profits(A, k)

    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = random.randint(1, n // 2)
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        n = random.randint(1, 10000)
        k = random.randint(1, n // 2)
    A = [random.randint(0, 99) for i in range(n)]
    print('n = %d, k = %d' % (n, k))
    print(max_k_pairs_profits(A, k))


if __name__ == '__main__':
    main()
