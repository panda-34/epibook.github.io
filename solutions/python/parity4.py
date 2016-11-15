# Parity4.h 848813e190b1b85a8e75107fe8513c3be38ad1a9
# @include
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
# @exclude
