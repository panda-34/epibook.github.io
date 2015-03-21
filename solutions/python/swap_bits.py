# swap_bits.h 848813e190b1b85a8e75107fe8513c3be38ad1a9
# swap_bits.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random

# @include
def swap_bits(x, i, j):
    # Extract the i-th and j-th bits, see if they differ.
    if (x >> i) & 1 != (x >> j) & 1:
        # Swap i-th and j-th bits by flipping them.
        # Select and flip bits by using a bit mask and XOR
        x ^= (1 << i) | (1 << j)
    return x
# @exclude


def simple_test():
    assert swap_bits(0b101111, 1, 4) == 0b111101
    assert swap_bits(0b11100, 0, 2) == 0b11001


def main():
    simple_test()
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        i = int(sys.argv[2])
        j = int(sys.argv[3])
    else:
        x = random.randint(0, sys.maxsize)
        i = random.randrange(sys.maxsize.bit_length())
        j = random.randrange(sys.maxsize.bit_length())
    print('x = %#x, i = %d, j = %d' % (x, i, j))
    print('%#x' % swap_bits(x, i, j))


if __name__ == '__main__':
    main()
