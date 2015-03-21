# Closest_int_same_bits.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def closest_int_same_bits(x):
    for i in range(63):
        if ((x >> i) & 1) ^ ((x >> (i + 1)) & 1):
            x ^= (1 << i) | (1 << (i + 1))  # swaps bit-i and bit-(i + 1).
            return x
    # Raise error if all bits of x are 0 or 1.
    raise ValueError('all bits are 0 or 1')
# @exclude


def count_bits_set_to1(x):
    count = 0
    while x:
        x &= (x - 1)
        count += 1
    return count


def main():
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
    else:
        x = random.randint(0, sys.maxsize)
    try:
        res = closest_int_same_bits(x)
        print(x, res)
        assert count_bits_set_to1(x) == count_bits_set_to1(res)
    except ValueError as e:
        print(x, e)


if __name__ == '__main__':
    main()
