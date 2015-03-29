# valid-palindrome.cc 69dab7578339012270872ba200cfff02f59ce894

# @include
def is_palindrome(s):
    # i moves forward, and j moves backward.
    i = 0
    j = len(s) - 1
    while i < j:
        # i and j both skip non-alphanumeric characters.
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True
# @exclude


def main():
    assert is_palindrome('A man, a plan, a canal: Panama')
    assert not is_palindrome('race a car')
    assert is_palindrome('Able was I, ere I saw Elba!')
    assert not is_palindrome('Ray a Ray')
    assert is_palindrome('')


if __name__ == '__main__':
    main()
