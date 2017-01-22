# Hash_dictionary.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import functools
import sys
import string
import random


def rand_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


# @include
def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda val, c: (val * MULT + ord(c)) % modulus, s,
                            0)


# @exclude


def main():
    s = sys.argv[1] if len(sys.argv) == 2 else rand_string(
        random.randint(1, 20))
    print('string =', s)
    print(string_hash(s, 1 << 16))


if __name__ == '__main__':
    main()
