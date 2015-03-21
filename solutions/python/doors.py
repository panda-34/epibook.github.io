# Doors.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import math


# @include
def is_door_open(i):
    sqrt_i = math.sqrt(i)
    floor_sqrt_i = math.floor(sqrt_i)
    return floor_sqrt_i ** 2 == i
# @exclude


# Pythonic solution
def is_door_open_pythonic(i):
    return math.sqrt(i).is_integer()


def check_answer(n):
    doors = [False] * (n + 1)  # False means closed door.
    for i in range(1, n+1):
        start = 0
        while start + i <= n:
            start += i
            doors[start] = not doors[start]

    for i in range(1, n+1):
        assert doors[i] == is_door_open(i) == is_door_open_pythonic(i)


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 1000)
    check_answer(n)


if __name__ == '__main__':
    main()
