# Can_string_be_palindrome.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import string
import can_string_be_palindrome_hash
import can_string_be_palindrome_sorting


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            s = sys.argv[1]
        else:
            s = rand_string(random.randint(1, 10))
        print(s)
        assert (can_string_be_palindrome_hash.can_string_be_a_palindrome(s) ==
                can_string_be_palindrome_sorting.can_string_be_a_palindrome(s) ==
                can_string_be_palindrome_sorting.can_string_be_a_palindrome_pythonic(s))


if __name__ == '__main__':
    main()
