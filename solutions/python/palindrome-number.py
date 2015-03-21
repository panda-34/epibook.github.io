# palindrome-number.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import math


# @include
def is_palindrome(x):
    if x < 0:
        return False
    if x == 0:
        return True
    k_num_digits = math.floor(math.log10(x)) + 1
    x_remaining = x
    msd_shift = 10 ** (k_num_digits - 1)
    for i in range(k_num_digits // 2):
        if x // msd_shift != x_remaining % 10:
            return False
        x %= msd_shift
        msd_shift //= 10
        x_remaining //= 10
    return True
# @exclude


def check_ans(x):
    s = str(x)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
        print(x, is_palindrome(x))
        assert check_ans(x) == is_palindrome(x)
    else:
        for _ in range(1000):
            x = random.randint(-99999, 99999)
            assert check_ans(x) == is_palindrome(x)


if __name__ == '__main__':
    main()
