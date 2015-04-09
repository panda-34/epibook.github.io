# Run_length_compression.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import itertools


# @include
def decoding(s):
    count = 0
    result = []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:  # c is a letter of alphabet.
            result.append(c * count)  # Appends count copies of c to result.
            count = 0
    return ''.join(result)


def encoding(s):
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            # Found new character so write the count of previous character.
            result.append(str(count) + s[i - 1])
            count = 1
        else:  # s[i] == s[i - 1].
            count += 1
    return ''.join(result)
# @exclude


def encoding_pythonic(s):
    result = []
    for c, g in itertools.groupby(s):
        count = sum(1 for i in g)
        result.append(str(count) + c)
    return ''.join(result)


def main():
    if len(sys.argv) == 3:
        print(encoding(sys.argv[1]), decoding(sys.argv[2]))
        assert encoding_pythonic(sys.argv[1]) == encoding(sys.argv[1])
    assert '4a1b3c2a' == encoding('aaaabcccaa') == encoding_pythonic('aaaabcccaa')
    assert 'eeeffffee' == decoding('3e4f2e')
    assert 'aaaaaaaaaaffffee' == decoding('10a4f2e')


if __name__ == '__main__':
    main()
