# GCD.h 98875343ac034c2bd2141da5f5c9c7e25c192d76
# GCD.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import fractions


# @include
def GCD(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif not x & 1 and not y & 1:  # x and y are even.
        return GCD(x >> 1, y >> 1) << 1
    elif not x & 1 and y & 1:  # x is even, y is odd.
        return GCD(x >> 1, y)
    elif x & 1 and not y & 1:  # x is odd, y is even.
        return GCD(x, y >> 1)
    elif x > y:  # Both x and y are odd, x > y.
        return GCD(x - y, y)
    return GCD(x, y - x)  # Both x and y are odd, x <= y.
# @exclude


def main():
    x = 18
    y = 12
    assert GCD(x, y) == 6
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(GCD(x, y))
        assert GCD(x, y) == fractions.gcd(x, y)
    else:
        for _ in range(1000):
            x = random.randint(1, sys.maxsize)
            y = random.randint(1, sys.maxsize)
            assert GCD(x, y) == fractions.gcd(x, y)


if __name__ == '__main__':
    main()
