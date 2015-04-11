# longest-valid-parentheses.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys


# @include
def longest_valid_parentheses(s):
    max_length = 0
    end = -1
    left_parentheses_indices = []
    for i in range(len(s)):
        if s[i] == '(':
            left_parentheses_indices.append(i)
        elif not left_parentheses_indices:
            end = i
        else:
            left_parentheses_indices.pop()
            start = left_parentheses_indices[-1] if left_parentheses_indices else end
            max_length = max(max_length, i - start)
    return max_length
# @exclude


def small_test():
    assert longest_valid_parentheses(')(((())()(()(') == 6
    assert longest_valid_parentheses('((())()(()(') == 6
    assert longest_valid_parentheses(')(') == 0
    assert longest_valid_parentheses('()') == 2
    assert longest_valid_parentheses('') == 0
    assert longest_valid_parentheses('()()())') == 6


def main():
    small_test()
    if len(sys.argv) == 2:
        s = sys.argv[1]
        print('s =', s)
        print(longest_valid_parentheses(s))


if __name__ == '__main__':
    main()
