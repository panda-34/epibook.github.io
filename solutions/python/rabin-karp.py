# rabin-karp.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import string


# @include
k_base = 26
k_mod = 997


def rabin_karp(t, s):
    if len(s) > len(t):
        return -1  # s is not a substring of t.

    t_hash = 0
    s_hash = 0  # Hash codes for the substring of t and s.
    power_s = 1  # The modulo result of k_base^|s|.
    for i in range(len(s)):
        power_s = power_s * k_base % k_mod if i else 1
        t_hash = (t_hash * k_base + ord(t[i])) % k_mod
        s_hash = (s_hash * k_base + ord(s[i])) % k_mod

    for i in range(len(s), len(t)):
        # In case of hash collision but two strings are not equal, checks the
        # two substrings are actually equal or not.
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)  # Found a match.

        # Uses rolling hash to compute the hash code.
        t_hash -= (ord(t[i - len(s)]) * power_s) % k_mod
        if t_hash < 0:
            t_hash += k_mod
        t_hash = (t_hash * k_base + ord(t[i])) % k_mod

    # Tries to match s and t[len(t) - len(s) : len(t) - 1].
    if t_hash == s_hash and t[len(t) - len(s) :] == s:
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


def main():
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
