# GCD.h 98875343ac034c2bd2141da5f5c9c7e25c192d76
# GCD.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import fractions
import gcd1
import gcd2


def main():
    x = 18
    y = 12
    assert gcd1.GCD(x, y) == 6
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(gcd1.GCD(x, y))
        assert gcd1.GCD(x, y) == fractions.gcd(x, y) == gcd2.GCD(x, y)
    else:
        for _ in range(1000):
            x = random.randint(1, sys.maxsize)
            y = random.randint(1, sys.maxsize)
            assert gcd1.GCD(x, y) == fractions.gcd(x, y) == gcd2.GCD(x, y)


if __name__ == '__main__':
    main()
