# Can_string_be_palindrome_hash.h 69dab7578339012270872ba200cfff02f59ce894
import collections


# @include
def can_string_be_a_palindrome(s):
    # Compute the frequency of each char in s.
    char_frequencies = collections.Counter(s)

    # A string can be permuted as a palindrome if and only if the number of
    # chars whose frequencies is odd is at most 1.
    odd_frequency_count = 0
    for f in char_frequencies.values():
        if f % 2:
            odd_frequency_count += 1
            if odd_frequency_count > 1:
                return False
    return True
# @exclude
