# insert-interval.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import collections
import sys
import random

# @include
Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    # Processes intervals in disjoint_intervals which come before new_interval.
    while i < len(disjoint_intervals
                  ) and new_interval.left > disjoint_intervals[i].right:
        result.append(disjoint_intervals[i])
        i += 1

    # Processes intervals in disjoint_intervals which overlap with new_interval.
    while i < len(disjoint_intervals
                  ) and new_interval.right >= disjoint_intervals[i].left:
        # If [a, b] and [c, d] overlap, union is [min(a, c),max(b, d)].
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right))
        i += 1
    result.append(new_interval)

    # Processes intervals in disjoint_intervals which come after new_interval.
    result += disjoint_intervals[i:]
    return result


# @exclude


def check_intervals(result):
    # Only check the intervals do not overlap with each other.
    assert all(result[i - 1].right < result[i].left
               for i in range(1, len(result)))


def small_test():
    A = [Interval(1, 5)]
    new_one = Interval(0, 3)
    result = add_interval(A, new_one)
    assert result == [Interval(0, 5)]
    new_one = Interval(0, 0)
    result = add_interval(A, new_one)
    assert result == [Interval(0, 0), Interval(1, 5)]


def main():
    small_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        A = []
        pre = 0
        for i in range(n):
            left = pre + random.randint(1, 10)
            right = left + random.randint(1, 10)
            temp = Interval(left, right)
            pre = temp.right
            A.append(temp)
        left = random.randint(0, 100)
        right = left + random.randint(0, 100)
        target = Interval(left, right)
        result = add_interval(A, target)
        check_intervals(result)


if __name__ == '__main__':
    main()
