# RPN.cpp 98875343ac034c2bd2141da5f5c9c7e25c192d76
# @include
def evaluate(RPN_expression):
    intermediate_results = []
    k_delimiter = ','

    for token in RPN_expression.split(k_delimiter):
        if token in '+-*/':
            y = intermediate_results.pop()
            x = intermediate_results.pop()
            if token == '+':
                intermediate_results.append(x + y)
            elif token == '-':
                intermediate_results.append(x - y)
            elif token == '*':
                intermediate_results.append(x * y)
            elif token == '/':
                intermediate_results.append(int(x / y))
        else:  # token is a number.
            intermediate_results.append(int(token))
    return intermediate_results[-1]
# @exclude


def main():
    assert 0 == evaluate('2,-10,/')
    assert -5 == evaluate('-10,2,/')
    assert 5 == evaluate('-10,-2,/')
    assert -5 == evaluate('5,10,-')
    assert 6 == evaluate('-10,-16,-')
    assert 12 == evaluate('10,2,+')
    assert 15 == evaluate('1,2,+,3,4,*,+')
    assert 42 == evaluate('1,2,3,4,5,+,*,+,+,3,4,*,+')


if __name__ == '__main__':
    main()
