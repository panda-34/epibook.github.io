# Square_root.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import math
import random


# @include
SMALLER, EQUAL, LARGER = range(3)

def square_root(x):
    # Decides the search range according to x's value relative to 1.0.
    if x < 1.0:
        left = x
        right = 1.0
    else:  # x >= 1.0.
        left = 1.0
        right = x

    # Keeps searching as long as left < right, within tolerance.
    while compare(left, right) == SMALLER:
        mid = left + 0.5 * (right - left)
        mid_squared = mid * mid
        if compare(mid_squared, x) == EQUAL:
            return mid
        elif compare(mid_squared, x) == LARGER:
            right = mid
        else:
            left = mid
    return left


def compare(a, b):
    # Uses normalization for precision problem.
    diff = a - b
    if b != 0.0:
        diff /= b
    if diff < -sys.float_info.epsilon:
        return SMALLER
    elif diff > sys.float_info.epsilon:
        return LARGER
    else:
        return EQUAL
# @exclude


def simple_test():
    assert compare(square_root(1.0), math.sqrt(1.0) == EQUAL)
    assert compare(square_root(2.0), math.sqrt(2.0) == EQUAL)
    assert compare(square_root(0.001), math.sqrt(0.001) == EQUAL)
    assert compare(square_root(0.5), math.sqrt(0.5) == EQUAL)
    assert compare(square_root(100000000.001), math.sqrt(100000000.001) == EQUAL)
    assert compare(square_root(1024.0), math.sqrt(1024.0) == EQUAL)


def main():
    simple_test()
    for _ in range(100000):
        if len(sys.argv) == 2:
            x = float(sys.argv[1])
        else:
            x = random.uniform(0.0, 100000000.0)
        res = [square_root(x), math.sqrt(x)]
        print('x is', x)
        print(res[0], res[1])
        assert compare(res[0], res[1]) == EQUAL


if __name__ == '__main__':
    main()
