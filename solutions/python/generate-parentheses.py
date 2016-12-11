# generate-parentheses.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def generate_balanced_parentheses(num_pairs):
    result = []
    directed_generate_balanced_parentheses(num_pairs, num_pairs, '', result)
    return result


def directed_generate_balanced_parentheses(
        num_left_parens_needed, num_right_parens_needed, valid_prefix, result):
    if not num_left_parens_needed and not num_right_parens_needed:
        result.append(valid_prefix)
        return

    if num_left_parens_needed > 0:  # Able to insert '('.
        directed_generate_balanced_parentheses(num_left_parens_needed - 1,
                                               num_right_parens_needed,
                                               valid_prefix + '(', result)

    if num_left_parens_needed < num_right_parens_needed:
        # Able to insert ')'.
        directed_generate_balanced_parentheses(num_left_parens_needed,
                                               num_right_parens_needed - 1,
                                               valid_prefix + ')', result)


# @exclude


def small_test():
    assert generate_balanced_parentheses(1) == ['()']
    result = generate_balanced_parentheses(2)
    assert result == ['(())', '()()'] or result == ['()()', '(())']


def main():
    small_test()
    if len(sys.argv) == 2:
        num_pairs = int(sys.argv[1])
    else:
        num_pairs = random.randint(0, 10)
    print('num_pairs =', num_pairs)
    result = generate_balanced_parentheses(num_pairs)
    print(*result)


if __name__ == '__main__':
    main()
