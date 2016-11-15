# Convert_base.cpp b4b3a70d8ab942579f85b4416f980d05831af969
from functools import reduce
import sys
import random
import string


# @include
def convert_base(num_as_string, b1, b2):
    is_negative = num_as_string[0] == '-'
    num_as_int = reduce(
        lambda x, c: x * b1 + (ord(c) - ord('0') if c.isdigit() else ord(c) - ord('A') + 10),
        num_as_string[1 if is_negative else 0:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


def construct_from_base(num_as_int, base):
    return '' if num_as_int == 0 else construct_from_base(
        num_as_int // base, base) + chr(
            ord('A') + num_as_int % base - 10
            if num_as_int % base >= 10 else ord('0') + num_as_int % base)
# @exclude


def rand_int_string(length):
    if length == 0:
        return '0'
    ret = []
    if random.randint(0, 1) == 1:
        ret.append('-')
    ret.append(chr(random.randint(ord('1'), ord('9'))))
    for _ in range(length - 1):
        ret.append(random.choice(string.digits))
    return ''.join(ret)


def main():
    if len(sys.argv) == 4:
        input_str = sys.argv[1]
        print(convert_base(input_str, int(sys.argv[2]), int(sys.argv[3])))
        assert input_str == convert_base(
            convert_base(input_str, int(sys.argv[2]), int(sys.argv[3])),
            int(sys.argv[3]), int(sys.argv[2]))
    else:
        for _ in range(1000):
            input_str = rand_int_string(random.randint(1, 9))
            base = random.randint(2, 16)
            print('input is %s, base1 = 10, base2 = %d, result = %s' %
                  (input_str, base, convert_base(input_str, 10, base)))
            assert input_str == convert_base(
                convert_base(input_str, 10, base), base, 10)


if __name__ == '__main__':
    main()
