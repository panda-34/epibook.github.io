# Reverse_bits.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import swap_bits


def reverse_x(x, n):
    i = 0
    j = n
    while i < j:
        x = swap_bits.swap_bits(x, i, j)
        i += 1
        j -= 1
    return x


precomputed_reverse = [reverse_x(i, 15) for i in range(1 << 16)]


# @include
def reverse_bits(x):
    k_word_size = 16
    k_bit_mask = 0xFFFF
    return (precomputed_reverse[x & k_bit_mask] << (3 * k_word_size) |
            precomputed_reverse[(x >> k_word_size) & k_bit_mask] << (2 * k_word_size) |
            precomputed_reverse[(x >> (2 * k_word_size)) & k_bit_mask] << k_word_size |
            precomputed_reverse[(x >> (3 * k_word_size)) & k_bit_mask])
# @exclude


def main():
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
        print('x = %#x, reverse x = %#x' % (x, reverse_bits(x)))
        print('%#x' % reverse_x(x, 63))
        assert reverse_bits(x) == reverse_x(x, 63)
    else:
        for _ in range(1000):
            x = random.randint(0, sys.maxsize)
            print('x = %#x, reverse x = %#x' % (x, reverse_bits(x)))
            assert reverse_bits(x) == reverse_x(x, 63)


if __name__ == '__main__':
    main()
