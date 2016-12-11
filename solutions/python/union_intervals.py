# Union_intervals.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import collections
import copy
import random

# @include
Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))


class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.left.val != other.left.val:
            return self.left.val < other.left.val
        # Left endpoints are equal, so now see if one is closed and the other open
        # - closed intervals should appear first.
        return self.left.is_closed and not other.left.is_closed


def union_of_intervals(intervals):
    # Empty input.
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort()
    curr = copy.copy(intervals[0])
    result = []
    for i in range(1, len(intervals)):
        if (intervals[i].left.val < curr.right.val or
            (intervals[i].left.val == curr.right.val and
             (intervals[i].left.is_closed or curr.right.is_closed))):
            if (intervals[i].right.val > curr.right.val or
                (intervals[i].right.val == curr.right.val and
                 intervals[i].right.is_closed)):
                curr.right = intervals[i].right
        else:
            result.append(curr)
            curr = copy.copy(intervals[i])
    result.append(curr)
    return result


# @exclude


def check_intervals(A):
    # Only check the intervals do not overlap with each other.
    assert all(A[i - 1].right.val < A[i].left.val or
               (A[i - 1].right.val == A[i].left.val and
                not A[i - 1].right.is_closed and not A[i].left.is_closed)
               for i in range(1, len(A)))


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 1000)
        A = []
        for i in range(n):
            left = Endpoint(bool(random.randrange(2)), random.randrange(10000))
            right = Endpoint(
                bool(random.randrange(2)),
                random.randrange(left.val + 1, left.val + 100))
            temp = Interval(left, right)
            A.append(temp)
        ret = union_of_intervals(A)
        if ret:
            check_intervals(ret)


if __name__ == '__main__':
    main()
