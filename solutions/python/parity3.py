# Parity3.h 848813e190b1b85a8e75107fe8513c3be38ad1a9
import parity1

_PRECOMPUTED_PARITY = [parity1.parity(i) for i in range(1 << 16)]

# @include
def parity(x):
    WORD_SIZE = 16
    BIT_MASK = 0xFFFF
    return (_PRECOMPUTED_PARITY[x >> (3 * WORD_SIZE)] ^
            _PRECOMPUTED_PARITY[(x >> (2 * WORD_SIZE)) & BIT_MASK] ^
            _PRECOMPUTED_PARITY[(x >> WORD_SIZE) & BIT_MASK] ^
            _PRECOMPUTED_PARITY[x & BIT_MASK])
# @exclude
