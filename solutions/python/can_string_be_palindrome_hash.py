# Can_string_be_palindrome_hash.h 69dab7578339012270872ba200cfff02f59ce894
import collections


# @include
def can_string_be_a_palindrome(s):
    # A string can be permuted as a palindrome if and only if the number of
    # chars whose frequencies is odd is at most 1.
    return sum(v % 2 for v in collections.Counter(s).values()) <= 1


# @exclude
