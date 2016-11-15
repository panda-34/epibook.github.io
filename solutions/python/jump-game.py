# jump-game.cc b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random


# @include
def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index
# @exclude


def small_test():
    assert can_reach_end([2, 3, 1, 1, 4])
    assert not can_reach_end([3, 2, 1, 0, 4])
    assert not can_reach_end([3, 2, 1, -10, 4])
    assert can_reach_end([2, 3, -1, -1, 4])
    assert not can_reach_end([2, 2, -1, -1, 100])


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 1000)

    A = [random.randint(1, 10) for i in range(n)]
    print(can_reach_end(A))


if __name__ == '__main__':
    main()
