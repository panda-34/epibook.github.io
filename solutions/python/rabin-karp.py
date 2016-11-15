# rabin-karp.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import string

# @include
k_mod = 997


def rabin_karp(t, s):
    if len(s) > len(t):
        return -1  # s is not a substring of t.

    BASE = 26
    t_hash, s_hash = 0, 0  # Hash codes for the substring of t and s.
    power_s = 1  # The modulo result of BASE^|s|.
    for i in range(len(s)):
        power_s = power_s * BASE if i else 1
        t_hash, s_hash = t_hash * BASE + ord(t[i]), s_hash * BASE + ord(s[i])

    for i in range(len(s), len(t)):
        # Checks the two substrings are actually equal or not, to protect against hash collision.h
        if t_hash == s_hash and t[i - len(s):i] == s:
            return i - len(s)  # Found a match.

        # Uses rolling hash to compute the hash code.
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    # Tries to match s and t[len(t) - len(s) : len(t) - 1].
    if t_hash == s_hash and t[len(t) - len(s):] == s:
        return len(t) - len(s)
    return -1  # s is not a substring of t.


# @exclude


def check_answer(t, s):
    i = 0
    while i + len(s) - 1 < len(t):
        find = True
        for j in range(len(s)):
            if t[i + j] != s[j]:
                find = False
                break
        if find:
            return i
        i += 1
    return -1  # find no matching.


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def simple_test():
    assert rabin_karp('GACGCCA', 'CGC') == 2
    assert rabin_karp('GATACCCATCGAGTCGGATCGAGT', 'GAG') == 10
    assert rabin_karp('FOOBARWIDGET', 'WIDGETS') == -1
    assert rabin_karp('A', 'A') == 0
    assert rabin_karp('A', 'B') == -1
    assert rabin_karp('A', '') == 0
    assert rabin_karp('ADSADA', '') == 0
    assert rabin_karp('', 'A') == -1
    assert rabin_karp('', 'AAA') == -1
    assert rabin_karp('A', 'AAA') == -1
    assert rabin_karp('AA', 'AAA') == -1
    assert rabin_karp('AAA', 'AAA') == 0
    assert rabin_karp('BAAAA', 'AAA') == 1
    assert rabin_karp('BAAABAAAA', 'AAA') == 1
    assert rabin_karp('BAABBAABAAABS', 'AAA') == 8
    assert rabin_karp('BAABBAABAAABS', 'AAAA') == -1
    assert rabin_karp('FOOBAR', 'BAR') > 0


def main():
    simple_test()
    if len(sys.argv) == 3:
        t = sys.argv[1]
        s = sys.argv[2]
        print('t =', t)
        print('s =', s)
        assert rabin_karp(t, s) == check_answer(t, s)
    else:
        for _ in range(10000):
            t = rand_string(random.randint(1, 1000))
            s = rand_string(random.randint(1, 20))
            print('t =', t)
            print('s =', s)
            ret1 = rabin_karp(t, s)
            ret2 = check_answer(t, s)
            print(ret1, ret2)
            assert rabin_karp(t, s) == check_answer(t, s)


if __name__ == '__main__':
    main()
