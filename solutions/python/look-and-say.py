# look-and-say.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import itertools


# @include
def look_and_say(n):
    s = '1'
    for i in range(1, n):
        s = next_number(s)
    return s

def next_number(s):
    ret = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        ret.append(str(count) + s[i])
        i += 1
    return ''.join(ret)
# @exclude


def look_and_say_pythonic(n):
    s = [1]
    for _ in range(1, n):
        new_s = []
        for k, g in itertools.groupby(s):
            count = sum(1 for i in g)
            new_s += [count, k]
        s = new_s
    return ''.join(map(str, s))


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 50)
    assert look_and_say(1) == '1'
    assert look_and_say(2) == '11'
    assert look_and_say(3) == '21'
    assert look_and_say(5) == '111221'
    print('n =', n)
    print(look_and_say(n))
    assert look_and_say(n) == look_and_say_pythonic(n)


if __name__ == '__main__':
    main()
