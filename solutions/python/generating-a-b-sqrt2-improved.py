# generating-a-b-sqrt2-improved.h 884568f491146065472fafc32923e8aa73dd8076
# generating-a-b-sqrt2-improved.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import math
import sortedcontainers


# @include
class ABSqrt2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

# @exclude

    def __hash__(self):
        return self.a ^ self.b

    def __repr__(self):
        return r'%d + %d \/2' % (self.a, self.b)


# @include


def generate_first_k_a_b_sqrt2(k):
    # Will store the first k numbers of the form a + b sqrt(2).
    result = [ABSqrt2(0, 0)]
    i = j = 0
    for n in range(1, k):
        result_i_plus_1 = ABSqrt2(result[i].a + 1, result[i].b)
        result_j_plus_sqrt2 = ABSqrt2(result[j].a, result[j].b + 1)
        result.append(min(result_i_plus_1, result_j_plus_sqrt2))
        if result_i_plus_1.val == result[-1].val:
            i += 1
        if result_j_plus_sqrt2.val == result[-1].val:
            j += 1
    return result


# @exclude


def golden(k):
    candidates = sortedcontainers.SortedSet()
    # Initial for 0 + 0 * sqrt(2).
    candidates.add(ABSqrt2(0, 0))

    result = []
    while len(result) < k:
        next_smallest = candidates[0]
        result.append(next_smallest)

        # Adds the next two numbers derived from next_smallest.
        candidates.add(ABSqrt2(next_smallest.a + 1, next_smallest.b))
        candidates.add(ABSqrt2(next_smallest.a, next_smallest.b + 1))
        candidates.remove(next_smallest)
    return result


def simple_test():
    ans = generate_first_k_a_b_sqrt2(8)
    assert 0.0 == ans[0].val
    assert 1.0 == ans[1].val
    assert math.sqrt(2.0) == ans[2].val
    assert 2.0 == ans[3].val
    assert 1.0 + math.sqrt(2.0) == ans[4].val
    assert 2.0 * math.sqrt(2.0) == ans[5].val
    assert 3.0 == ans[6].val
    assert 2.0 + math.sqrt(2.0) == ans[7].val


def main():
    simple_test()
    for times in range(1000):
        if len(sys.argv) == 2:
            k = int(sys.argv[1])
        else:
            k = random.randint(1, 10000)
        ans = generate_first_k_a_b_sqrt2(k)
        assert len(ans) == k
        for i, a in enumerate(ans):
            print(a.a, a.b, a.val)
            if i > 0:
                assert a.val >= ans[i - 1].val
        gold_res = golden(k)
        for i in range(k):
            assert ans[i].val == gold_res[i].val


if __name__ == '__main__':
    main()
