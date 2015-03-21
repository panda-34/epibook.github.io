# Division.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


def divide_x_y_bsearch(x, y):
    if x < y:
        return 0

    power_left = 0
    power_right = x.bit_length()
    power_mid = -1
    while power_left < power_right:
        tmp = power_mid
        power_mid = power_left + (power_right - power_left) // 2
        if tmp == power_mid:
            break

        yshift = y << power_mid
        if yshift > x:
            power_right = power_mid
        elif yshift < x:
            power_left = power_mid
        else:
            return 1 << power_mid
    part = 1 << power_left
    return part | divide_x_y_bsearch(x - (y << power_left), y)


# @include
def divide_x_y(x, y):
    result = 0
    while x >= y:
        power = 1
        while (y << power) <= x:
            power += 1

        result += 1 << (power - 1)
        x -= y << (power - 1)
    return result
# @exclude


def simple_test():
    assert divide_x_y(64, 1) == 64
    assert divide_x_y(64, 2) == 32
    assert divide_x_y(64, 3) == 21
    assert divide_x_y(64, 4) == 16
    assert divide_x_y(64, 5) == 12
    assert divide_x_y(65, 2) == 32
    assert divide_x_y(2600540749, 2590366779) == 1
    assert divide_x_y_bsearch(4, 2)
    assert divide_x_y_bsearch(64, 1) == 64
    assert divide_x_y_bsearch(64, 2) == 32
    assert divide_x_y_bsearch(64, 3) == 21
    assert divide_x_y_bsearch(64, 4) == 16
    assert divide_x_y_bsearch(64, 5) == 12
    assert divide_x_y_bsearch(65, 2) == 32
    assert divide_x_y_bsearch(9444, 4714) == 2
    assert divide_x_y_bsearch(8186, 19) == 430
    assert divide_x_y_bsearch(8186, 19) == 430


def main():
    simple_test()
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        assert x // y == divide_x_y(x, y) == divide_x_y_bsearch(x, y)
    else:
        for times in range(100000):
            x = random.randint(0, sys.maxsize)
            y = random.randint(1, sys.maxsize)  # ensure no divide by 0.
            print('times = %d, x = %d, y = %d' % (times, x, y))
            print('first = %d, second = %d' % (x // y, divide_x_y(x, y)))
            assert x // y == divide_x_y(x, y) == divide_x_y_bsearch(x, y)


if __name__ == '__main__':
    main()
