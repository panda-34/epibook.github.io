# container-with-most-water.cc 884568f491146065472fafc32923e8aa73dd8076
import sys
import random


# @include
def get_max_trapped_water(heights):
    i = 0
    j = len(heights) - 1
    max_water = 0
    while i < j:
        width = j - i
        max_water = max(max_water, width * min(heights[i], heights[j]))
        if heights[i] > heights[j]:
            j -= 1
        elif heights[i] < heights[j]:
            i += 1
        else:  # heights[i] == heights[j].
            i += 1
            j -= 1
    return max_water
# @exclude


# O(n^2) checking answer.
def check_ans(heights):
    res = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            res = max(res, min(heights[i], heights[j]) * (j - i))
    return res


def small_test():
    A = (1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1)
    assert 48 == get_max_trapped_water(A)


def main():
    small_test()
    for times in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(2, 10000)
        heights = [random.randint(1, 1000) for i in range(n)]
        print(get_max_trapped_water(heights))
        assert get_max_trapped_water(heights) == check_ans(heights)


if __name__ == '__main__':
    main()
