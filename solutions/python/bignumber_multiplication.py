# Bignumber_multiplication.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import string


# @include
def multiply(num1, num2):
    is_positive = True
    if num1[0] == '-':
        is_positive = not is_positive
        num1 = num1[1:]
    if num2[0] == '-':
        is_positive = not is_positive
        num2 = num2[1:]

    # Reverses num1 and num2 to make multiplication easier.
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    # Converts result to string in reverse order, skips the first 0s and
    # keeps one 0 if all are 0s.
    i = len(num1) + len(num2) - 1
    while result[i] == 0 and i != 0:
        i -= 1
    ss = []
    if not is_positive and result[i] != 0:  # It won't print '-0'.
        ss.append('-')
    while i >= 0:
        ss.append(str(result[i]))
        i -= 1
    return ''.join(ss)
# @exclude


def rand_string(length):
    if length == 0:
        return '0'
    ret = []
    if random.randint(0, 1) == 1:
        ret.append('-')
    ret.append(chr(random.randint(ord('1'), ord('9'))))
    for _ in range(length-1):
        ret.append(random.choice(string.digits))
    return ''.join(ret)


def simple_test():
    assert multiply('0', '1000') == '0'
    print(multiply('131412', '-1313332'))
    assert multiply('131412', '-1313332') == '-172587584784'


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 3:
            s1 = sys.argv[1]
            s2 = sys.argv[2]
        else:
            s1 = rand_string(random.randint(0, 19))
            s2 = rand_string(random.randint(0, 19))

        res = multiply(s1, s2)
        print(s1, '*', s2, '=', res)
        result = int(s1) * int(s2)
        print('answer =', result)
        assert result == int(res)


if __name__ == '__main__':
    main()
