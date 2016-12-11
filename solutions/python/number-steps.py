# number-steps.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def number_of_ways_to_top(top, maximum_step):
    return compute_number_of_ways_to_h(top, maximum_step, [0] * (top + 1))


def compute_number_of_ways_to_h(h, maximum_step, number_of_ways_to_h):
    if h <= 1:
        return 1

    if number_of_ways_to_h[h] == 0:
        i = 1
        while i <= maximum_step and h - i >= 0:
            number_of_ways_to_h[h] += compute_number_of_ways_to_h(
                h - i, maximum_step, number_of_ways_to_h)
            i += 1
    return number_of_ways_to_h[h]


# @exclude


def main():
    assert 5 == number_of_ways_to_top(4, 2)
    assert 1 == number_of_ways_to_top(1, 2)
    assert 1 == number_of_ways_to_top(0, 3)
    if len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        n = random.randint(1, 20)
        k = random.randint(1, n)
    print('n = %d, k = %d' % (n, k))
    print(number_of_ways_to_top(n, k))


if __name__ == '__main__':
    main()
