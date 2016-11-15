# MultiplyShiftAdd.cpp 98875343ac034c2bd2141da5f5c9c7e25c192d76
import sys
import random


# @include
def multiply(x, y):
    sum = 0
    while x:  # Examines each bit of x.
        if x & 1:
            sum = add(sum, y)
        x >>= 1
        y <<= 1
    return sum


def add(a, b):
    sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
    while temp_a or temp_b:
        ak, bk = a & k, b & k
        carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
        sum |= ak ^ bk ^ carryin
        carryin = carryout << 1
        k <<= 1
        temp_a >>= 1
        temp_b >>= 1
    return sum | carryin
# @exclude


def main():
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        res = multiply(x, y)
        assert res == x * y
        print('x = %d, y = %d, prod = %d' % (x, y, res))
    else:
        for _ in range(100000):
            x, y = random.randint(0, 65534), random.randint(0, 65534)
            prod = multiply(x, y)
            assert prod == x * y
            print('x = %d, y = %d, prod = %d' % (x, y, prod))


if __name__ == '__main__':
    main()
