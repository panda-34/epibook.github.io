# power-x-y.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# 0 means equal, -1 means smaller, 1 means larger.
def compare(a, b):
    # Uses normalization for precision problem.
    diff = (a - b) / b
    if diff < -sys.float_info.epsilon:
        return -1
    if diff > sys.float_info.epsilon:
        return 1
    return 0


# @include
def power_x_y(x, y):
    result = 1.0
    power = y
    if y < 0:
        power = -power
        x = 1.0 / x
    while power:
        if power & 1:
            result *= x
        x *= x
        power >>= 1
    return result
# @exclude


def main():
    if len(sys.argv) == 3:
        x = float(sys.argv[1])
        y = int(sys.argv[2])
        print('%g^%d: %g, %g' % (x, y, power_x_y(x, y), x ** y))
        assert compare(power_x_y(x, y), x ** y) == 0
    else:
        for _ in range(10000):
            x = random.uniform(0.0, 10.0)
            y = random.randint(-128, 128)
            print('%g^%d: %g, %g' % (x, y, power_x_y(x, y), x ** y))
#            assert compare(power_x_y(x, y), x ** y) == 0


if __name__ == '__main__':
    main()
