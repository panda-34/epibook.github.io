# Regular_expression.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
def is_match(regex, s):
    # Case (2.): regex starts with '^'.
    if regex[0] == '^':
        return is_match_here(regex, 1, s, 0)

    for i in range(len(s) + 1):
        if is_match_here(regex, 0, s, i):
            return True
    return False


def is_match_here(regex, regex_offset, s, s_offset):
    if regex_offset == len(regex):
        # Case (1.): Empty regex matches all strings.
        return True

    if regex_offset == len(regex) - 1 and regex[regex_offset] == '$':
        # Case (2.): Reach the end of regex, and last char is '$'.
        return s_offset == len(s)

    if len(regex) - regex_offset >= 2 and regex[regex_offset + 1] == '*':
        # Case (3.): A '*' match.
        # Iterate through s, checking '*' condition, if '*' condition holds,
        # performs the remaining checks.
        i = s_offset + 1
        while i < len(s) and regex[regex_offset] in ('.', s[i - 1]):
            if is_match_here(regex, regex_offset + 2, s, i):
                return True
            i += 1
        # See '*' matches zero character in s[s_offset : len(s) - 1].
        return is_match_here(regex, regex_offset + 2, s, s_offset)

    # Case (4.): regex begins with single character match.
    return (s_offset < len(s) and regex[regex_offset] in ('.', s[s_offset]) and
            is_match_here(regex, regex_offset + 1, s, s_offset + 1))
# @exclude


def main():
    assert is_match('.', 'a')
    assert is_match('a', 'a')
    assert not is_match('a', 'b')
    assert is_match('a.9', 'aW9')
    assert not is_match('a.9', 'aW19')
    assert is_match('^a.9', 'aW9')
    assert not is_match('^a.9', 'baW19')
    assert is_match('.*', 'a')
    assert is_match('.*', '')
    assert is_match('c*', 'c')
    assert not is_match('aa*', 'c')
    assert is_match('ca*', 'c')
    assert is_match('.*', 'asdsdsa')
    assert is_match('9$', 'xxxxW19')

    assert is_match('.*a', 'ba')

    assert is_match('.*a', 'ba')
    assert is_match('^a.*9$', 'axxxxW19')

    assert is_match('^a.*W19$', 'axxxxW19')
    assert is_match('.*a.*W19', 'axxxxW19123')
    assert not is_match('.*b.*W19', 'axxxxW19123')
    assert is_match('n.*', 'n')
    assert is_match('a*n.*', 'an')
    assert is_match('a*n.*', 'ana')
    assert is_match('a*n.*W19', 'anaxxxxW19123')
    assert is_match('.*a*n.*W19', 'asdaaadnanaxxxxW19123')
    assert is_match('.*.*.a*n.*W19', 'asdaaadnanaxxxxW19123')


if __name__ == '__main__':
    main()
