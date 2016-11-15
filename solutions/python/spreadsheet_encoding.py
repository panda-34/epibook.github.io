# Spreadsheet_encoding.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
from functools import reduce
import sys
import random
import string


def rand_string(length):
    ret = (random.choice(string.ascii_uppercase) for _ in range(length))
    return ''.join(ret)


# @include
def ss_decode_col_id(col):
    return reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col,
                  0)
# @exclude


def simple_test():
    assert 1 == ss_decode_col_id('A')
    assert 2 == ss_decode_col_id('B')
    assert 26 == ss_decode_col_id('Z')
    assert 27 == ss_decode_col_id('AA')


def main():
    simple_test()
    if len(sys.argv) == 2:
        print(sys.argv[1], ss_decode_col_id(sys.argv[1]))
    else:
        s = rand_string(random.randint(1, 5))
        print(s, ss_decode_col_id(s))


if __name__ == '__main__':
    main()
