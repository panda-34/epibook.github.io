# jump-game.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# @include
def can_reach(A):
    furthest_reach = 0
    i = 0
    while i <= furthest_reach and furthest_reach < len(A) - 1:
        furthest_reach = max(furthest_reach, A[i] + i)
        i += 1
    return furthest_reach >= len(A) - 1
# @exclude


def small_test():
    assert can_reach([2, 3, 1, 1, 4])
    assert not can_reach([3, 2, 1, 0, 4])
    assert not can_reach([3, 2, 1, -10, 4])
    assert can_reach([2, 3, -1, -1, 4])
    assert not can_reach([2, 2, -1, -1, 100])


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 1000)

    A = [random.randint(1, 10) for i in range(n)]
    print(can_reach(A))


if __name__ == '__main__':
    main()
