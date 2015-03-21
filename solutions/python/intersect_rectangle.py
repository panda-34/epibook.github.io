# Intersect_rectangle.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import collections


# @include
Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R, S):
    if is_intersect(R, S):
        return Rectangle(max(R.x, S.x), max(R.y, S.y),
                         min(R.x + R.width, S.x + S.width) - max(R.x, S.x),
                         min(R.y + R.height, S.y + S.height) - max(R.y, S.y))
    else:
        return Rectangle(0, 0, -1, -1)  # No intersection.


def is_intersect(R, S):
    return (R.x <= S.x + S.width and R.x + R.width >= S.x and
            R.y <= S.y + S.height and R.y + R.height >= S.y)
# @exclude


def main():
    for _ in range(10000):
        if len(sys.argv) == 9:
            R = Rectangle(*map(int, sys.argv[1:5]))
            S = Rectangle(*map(int, sys.argv[5:9]))
        else:
            R = Rectangle(*(random.randint(1, 100) for i in range(4)))
            S = Rectangle(*(random.randint(1, 100) for i in range(4)))

        # Intersect rectangle.
        res = is_intersect(R, S)
        print(res)
        ans = intersect_rectangle(R, S)
        print('ans:', ans)
        assert res == False or (ans.width >= 0 and ans.height >= 0)


if __name__ == '__main__':
    main()
