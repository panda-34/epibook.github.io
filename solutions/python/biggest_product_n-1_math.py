# Biggest_product_n-1_math.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# @include
def find_biggest_n_minus_one_product(A):
    zero_count = 0
    zero_idx = -1
    positive_count = 0
    smallest_positive_idx = -1
    negative_count = 0
    smallest_negative_idx = -1
    biggest_negative_idx = -1

    for i in range(len(A)):
        if A[i] < 0:
            negative_count += 1
            if smallest_negative_idx == -1 or A[i] < A[smallest_negative_idx]:
                smallest_negative_idx = i
            if biggest_negative_idx == -1 or A[biggest_negative_idx] < A[i]:
                biggest_negative_idx = i
        elif A[i] == 0:
            zero_idx = i
            zero_count += 1
        else:  # A[i] > 0.
            positive_count += 1
            if smallest_positive_idx == -1 or A[i] < A[smallest_positive_idx]:
                smallest_positive_idx = i

    # Try to find a number whose elimination could maximize the product of
    # the remaining (n - 1) numbers.
    # x stores the idx of eliminated one.
    if zero_count >= 2:
        return 0
    elif zero_count == 1:
        if negative_count & 1:  # Odd number of negatives.
            return 0
        else:
            x = zero_idx
    else:  # No zero in A.
        if negative_count & 1:  # Odd number of negatives.
            x = biggest_negative_idx
        else:  # Even number of negatives.
            if positive_count > 0:
                x = smallest_positive_idx
            else:
                x = smallest_negative_idx

    product = 1
    for i, a in enumerate(A):
        if i != x:
            product *= a
    return product
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
    print(max_product)
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
        print(res)
        assert res == check_ans(A)


if __name__ == '__main__':
    main()
