# snake-string.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import string


# @include
def snake_string(s):
    result = []
    # Outputs the first row, i.e., s[1], s[5], s[9], ...
    for i in range(1, len(s), 4):
        result.append(s[i])

    # Outputs the second row, i.e., s[0], s[2], s[4], ...
    for i in range(0, len(s), 2):
        result.append(s[i])

    # Outputs the third row, i.e., s[3], s[7], s[11], ...
    for i in range(3, len(s), 4):
        result.append(s[i])

    return ''.join(result)
# @exclude


def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]


def rand_string(length):
    ret = (random.choice(string.ascii_uppercase) for i in range(length))
    return ''.join(ret)


def small_test():
    assert snake_string('Hello World!') == 'e lHloWrdlo!'
    assert snake_string_pythonic('Hello World!') == 'e lHloWrdlo!'


def main():
    small_test()
    if len(sys.argv) == 2:
        s = sys.argv[1]
    else:
        s = rand_string(random.randint(1, 100))
    print(snake_string(s))
    assert snake_string(s) == snake_string_pythonic(s)


if __name__ == '__main__':
    main()
