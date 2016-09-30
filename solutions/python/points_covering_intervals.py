# Points_covering_intervals.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import sortedcontainers

# @include
class Interval:

    def __init__(self, left=0, right=0):
        self.left = left
        self.right = right
# @exclude

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __repr__(self):
        return '(%s, %s)' % (self.left, self.right)

    def __hash__(self):
        return self.left ^ self.right
# @include


def left_comp(interval):
    return interval.left, interval.right


def right_comp(interval):
    return interval.right, interval.left


def find_minimum_visits(intervals):
    L = sortedcontainers.SortedSet(intervals, key=left_comp)
    R = sortedcontainers.SortedSet(intervals, key=right_comp)

    S = []
    while L and R:
        b = R[0].right
        S.append(b)

        # Removes the intervals which intersect with R[0]
        while L and L[0].left <= b:
            R.remove(L[0])
            del L[0]
    return S
# @exclude


# O(n^2) checking solution
def check_ans(intervals, ans):
    is_visited = [False] * len(intervals)
    for a in ans:
        for i, interval in enumerate(intervals):
            if interval.left <= a <= interval.right:
                is_visited[i] = True
    assert all(is_visited)


def simple_test():
    intervals = [
        Interval(1, 4),
        Interval(2, 8),
        Interval(3, 6),
        Interval(3, 5),
        Interval(7, 10),
        Interval(9, 11)]
    ans = find_minimum_visits(intervals)
    assert ans == [4, 10]
    intervals = [
        Interval(1, 2),
        Interval(2, 3),
        Interval(3, 4),
        Interval(4, 5),
        Interval(5, 6),
        Interval(6, 7)]
    ans = find_minimum_visits(intervals)
    assert ans == [2, 4, 6]


def main():
    simple_test()
    for times in range(1000):
        print('Test', times)
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        A = []
        for i in range(n):
            left = random.randrange(10000)
            right = random.randint(left + 1, left + 100)
            A.append(Interval(left, right))
        ans = find_minimum_visits(A)
        check_ans(A, ans)


if __name__ == '__main__':
    main()
