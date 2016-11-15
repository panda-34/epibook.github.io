# valid-parentheses.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys


# @include
def is_well_formed(s):
    left_chars = []
    for c in s:
        if c in '({[':
            left_chars.append(c)
        else:
            if not left_chars:
                return False  # Unmatched right char.
            if ((c == ')' and left_chars[-1] != '(') or
                (c == '}' and left_chars[-1] != '{') or
                (c == ']' and left_chars[-1] != '[')):
                return False  # Mismatched chars.
            left_chars.pop()
    return not left_chars
# @exclude


def small_test():
    assert is_well_formed('()')
    assert is_well_formed('()[]{}')
    assert is_well_formed('[()[]]{}')
    assert is_well_formed('(()[]{()[]{}{}})')
    assert not is_well_formed('([)]')
    assert not is_well_formed('[')
    assert not is_well_formed('(()[]{()[]{})({}})')


def main():
    small_test()
    if len(sys.argv) == 2:
        print(is_well_formed(sys.argv[1]))


if __name__ == '__main__':
    main()
