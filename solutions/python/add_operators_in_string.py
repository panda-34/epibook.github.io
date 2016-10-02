# Add_operators_in_string.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
def expression_synthesis(digits, target):
    operators = []
    operands = []
    return directed_expression_synthesis(digits, target, 0, 0, operands, operators)


def directed_expression_synthesis(digits, target, current_term,
                                  offset, operands, operators):
    current_term = current_term * 10 + digits[offset]
    if offset == len(digits) - 1:
        operands.append(current_term)
        if evaluate(operands, operators) == target:  # Found a match.
            # @exclude
            operand_it = iter(operands)
            print(next(operand_it), end='')
            for oper in operators:
                print('', oper, next(operand_it), end='')
            print(' =', target)
            # @include
            return True
        del operands[-1]
        return False

    # No operator.
    if directed_expression_synthesis(digits, target, current_term, offset + 1,
                                     operands, operators):
        return True
    # Tries multiplication operator '*'.
    operands.append(current_term)
    operators.append('*')
    if directed_expression_synthesis(digits, target, 0, offset + 1,
                                     operands, operators):
        return True
    del operands[-1]
    del operators[-1]
    # Tries addition operator '+'.
    operands.append(current_term)
    # First check feasibility of plus operator.
    if target - evaluate(operands, operators) <= remaining_int(digits, offset + 1):
        operators.append('+')
        if directed_expression_synthesis(digits, target, 0, offset + 1,
                                         operands, operators):
            return True
        del operators[-1]
    del operands[-1]
    return False


# Calculates the int represented by digits[idx:].
def remaining_int(digits, idx):
    val = 0
    for i in range(idx, len(digits)):
        val = val * 10 + digits[i]
    return val


def evaluate(operands, operators):
    intermediate_operands = []
    operand_it = iter(operands)
    intermediate_operands.append(next(operand_it))
    # Evaluates '*' first.
    for oper in operators:
        if oper == '*':
            product = intermediate_operands[-1] * next(operand_it)
            intermediate_operands[-1] = product
        else:  # oper == '+'.
            intermediate_operands.append(next(operand_it))

    # Evaluates '+' second.
    return sum(intermediate_operands)
# @exclude


def main():
    A = [2, 3, 4]
    k = 4
    assert not expression_synthesis(A, k)
    A = [1, 2, 3, 4]
    k = 11
    assert expression_synthesis(A, k)
    A = [1, 2, 3, 2, 5, 3, 7, 8, 5, 9]
    k = 995
    assert expression_synthesis(A, k)
    A = [5, 2, 3, 4, 1]
    k = 20
    assert expression_synthesis(A, k)
    A = [1, 1, 2, 3]
    k = 124
    assert expression_synthesis(A, k)


if __name__ == '__main__':
    main()
