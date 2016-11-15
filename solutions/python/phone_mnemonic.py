# Phone_mnemonic.cpp 69dab7578339012270872ba200cfff02f59ce894
import sys
import random
import string
import itertools


# @include
def phone_mnemonic(phone_number):
    partial_mnemonic = [0] * len(phone_number)
    mnemonics = []
    phone_mnemonic_helper(phone_number, 0, partial_mnemonic, mnemonics)
    return mnemonics


# The mapping from digit to corresponding characters.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic_helper(phone_number, digit, partial_mnemonic, mnemonics):
    if digit == len(phone_number):
        # All digits are processed, so add partial_mnemonic to mnemonics.
        # (We add a copy since subsequent calls modify partial_mnemonic.)
        mnemonics.append(''.join(partial_mnemonic))
    else:
        # Try all possible characters for this digit.
        for c in MAPPING[ord(phone_number[digit]) - ord('0')]:
            partial_mnemonic[digit] = c
            phone_mnemonic_helper(phone_number, digit + 1, partial_mnemonic,
                                  mnemonics)
# @exclude


# Pythonic solution
def phone_mnemonic_pythonic(phone_number):
    letters = (MAPPING[int(digit)] for digit in phone_number)
    return [''.join(mnemonic) for mnemonic in itertools.product(*letters)]


def rand_string(length):
    ret = (random.choice(string.digits) for i in range(length))
    return ''.join(ret)


def main():
    if len(sys.argv) == 2:
        num = sys.argv[1]
    else:
        num = rand_string(10)
    result = phone_mnemonic(num)
    print('number =', num)
    for s in result:
        print(s)
    assert result == phone_mnemonic_pythonic(num)


if __name__ == '__main__':
    main()
