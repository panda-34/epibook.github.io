# Hash_dictionary.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import string
import random


def rand_string(length):
    ret = (random.choice(string.ascii_letters) for i in range(length))
    return ''.join(ret)


# @include
def string_hash(str, modulus):
    k_mult = 997
    val = 0
    for c in str:
        val = (val * k_mult + ord(c)) % modulus
    return val


# @exclude


def main():
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = rand_string(random.randint(1, 20))
    print('string =', s)
    print(string_hash(s, 1 << 16))


if __name__ == '__main__':
    main()
