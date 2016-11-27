# palindrome-partitioning-min-cuts.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string


# @include
def min_cuts(s):
    is_palindrome = [[False] * len(s) for i in s]
    T = list(range(len(s) - 1, -2, -1))
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i < 2 or is_palindrome[i + 1][j - 1]):
                is_palindrome[i][j] = True
                T[i] = min(T[i], 1 + T[j + 1])
    return T[0]
# @exclude


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def small_test():
    assert 1 == min_cuts('aab')
    assert 0 == min_cuts('bb')
    assert 3 == min_cuts('cabababcbc')
    assert 42 == min_cuts('eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj')


def main():
    small_test()
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = rand_string(random.randint(0, 10))
        print('times =', min_cuts(s))


if __name__ == '__main__':
    main()
