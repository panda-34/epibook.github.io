# Uniform_random_number_generation.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


def zero_one_random():
    return random.randrange(2)


# @include
def uniform_random(a, b):
    t = b - a + 1
    while True:
        res = 0
        i = 0
        while (1 << i) < t:
            # zero_one_random() is the system-provided random number generator.
            res = (res * 2) | zero_one_random()
            i += 1
        if res < t:
            break
    return res + a
# @exclude


def main():
    for _ in range(1000):
        if len(sys.argv) == 3:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
        else:
            a = random.randint(0, 99)
            b = random.randint(a + 1, a + 100)
        x = uniform_random(a, b)
        print('a =', a, 'b =', b)
        print('random result =', x)
        assert a <= x <= b


if __name__ == '__main__':
    main()
