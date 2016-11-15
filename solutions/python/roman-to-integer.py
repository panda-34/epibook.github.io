# roman-to-integer.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys


# @include
def roman_to_integer(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    sum = T[s[-1]]
    for i in range(len(s) - 2, -1, -1):
        sum += -T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]
    return sum
# @exclude


def main():
    assert 7 == roman_to_integer('VII')
    assert 184 == roman_to_integer('CLXXXIV')
    assert 9 == roman_to_integer('IX')
    assert 40 == roman_to_integer('XL')
    assert 60 == roman_to_integer('LX')
    assert 1500 == roman_to_integer('MD')
    assert 400 == roman_to_integer('CD')
    assert 1900 == roman_to_integer('MCM')
    assert 9919 == roman_to_integer('MMMMMMMMMCMXIX')
    if len(sys.argv) == 2:
        print(sys.argv[1], 'equals to', roman_to_integer(sys.argv[1]))


if __name__ == '__main__':
    main()
