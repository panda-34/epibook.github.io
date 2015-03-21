# MultiplyShiftAdd.cpp 98875343ac034c2bd2141da5f5c9c7e25c192d76
import sys
import random


# @include
def multiply_no_operator(x, y):
    res = 0
    while x:  # Examines each bit of x.
        if x & 1:
            res = add_no_operator(res, y)
        x >>= 1
        y <<= 1
    return res


def add_no_operator(a, b):
    res = 0
    carryin = 0
    k = 1
    temp_a = a
    temp_b = b
    while temp_a or temp_b:
        ak = a & k
        bk = b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        res |= ak ^ bk ^ carryin
        carryin = carryout << 1
        k <<= 1
        temp_a >>= 1
        temp_b >>= 1
    return res | carryin
# @exclude


def main():
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        res = multiply_no_operator(x, y)
        assert res == x * y
        print('x = %d, y = %d, prod = %d' % (x, y, res))
    else:
        for _ in range(100000):
            x = random.randint(0, 65534)
            y = random.randint(0, 65534)
            res = multiply_no_operator(x, y)
            assert res == x * y
            print('x = %d, y = %d, prod = %d' % (x, y, res))


if __name__ == '__main__':
    main()
