# Line_most_points.cpp dd7adc0dbf96e35e29defe6d31337c155c450a2f
import sys
import random
import collections
import fractions

# @include
Point = collections.namedtuple("Point", ("x", "y"))
Rational = collections.namedtuple("Rational", ("numerator", "denominator"))


def get_canonical_form(a, b):
    gcd = fractions.gcd(abs(a), abs(b))
    a //= gcd
    b //= gcd
    return Rational(-a, -b) if b < 0 else Rational(a, b)


# Line function of two points, a and b, and the equation is
# y = x(b.y - a.y) / (b.x - a.x) + (b.x * a.y - a.x * b.y) / (b.x - a.x).
class Line:
    def __init__(self, a, b):
        # slope is a rational number. Note that if the line is parallel to y-axis
        # that we store 1/0.
        self.slope = (get_canonical_form(b.y - a.y, b.x - a.x)
                      if a.x != b.x else Rational(1, 0))
        # intercept is a rational number for the y-intercept unless
        # the line is parallel to y-axis in which case it is the x-intercept.
        self.intercept = (get_canonical_form(b.x * a.y - a.x * b.y, b.x - a.x)
                          if a.x != b.x else Rational(a.x, 1))

    def __eq__(self, other):
        return self.slope == other.slope and self.intercept == other.intercept

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.slope) ^ hash(self.intercept)
# @exclude

    def __repr__(self):
        return ' '.join(
            map(str, (self.slope.numerator, self.slope.denominator,
                      self.intercept.numerator, self.intercept.denominator)))


# n^3 checking
def check(P):
    max_count = 0
    for i in range(len(P) - 1):
        for j in range(i + 1, len(P)):
            count = 2
            temp = Line(P[i], P[j])
            for k in range(j + 1, len(P)):
                if Line(P[i], P[k]) == temp:
                    count += 1
            max_count = max(max_count, count)
    return max_count


# @include
def find_line_with_most_points(P):
    # Add all possible lines into hash table.
    table = collections.defaultdict(set)
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            l = Line(P[i], P[j])
            table[l].add(P[i])
            table[l].add(P[j])
    line_max_points = max(table.items(), key=lambda x: len(x[1]))
    # @exclude
    res = check(P)
    assert res == len(line_max_points[1])
    # @include
    return line_max_points[0]


# @exclude


def main():
    for times in range(100):
        print(times)
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 100)
        points = []
        t = set()
        while len(t) < n:
            p = Point(random.randint(0, 999), random.randint(0, 999))
            if p not in t:
                points.append(p)
                t.add(p)
        #print(points)
        l = find_line_with_most_points(points)
        print(l)


if __name__ == '__main__':
    main()
