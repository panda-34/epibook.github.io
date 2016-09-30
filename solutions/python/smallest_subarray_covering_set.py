# Smallest_subarray_covering_set_stream.h bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# Smallest_subarray_covering_set.h bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# Smallest_subarray_covering_set.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import collections
import random
import string
from linked_list_prototype import LinkedList


# @include
def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.defaultdict(int)
    for keyword in keywords:
        keywords_to_cover[keyword] += 1
    result = (-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # Keeps advancing left until keywords_to_cover does not contain all
        # keywords.
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1
    return result


def find_smallest_subarray_covering_subset(sin, query_strings):
    # Tracks the last occurrence (index) of each string in query_strings.
    loc = LinkedList()
    d = {s: None for s in query_strings}
    res = (-1, -1)
    for idx, s in enumerate(sin):
        if s in d:
            it = d[s]
            if it is not None:
                # Explicitly remove s so that when we add it, it's the string most
                # recently added to loc.
                loc.erase(it)
            loc.emplace_back(idx)
            d[s] = loc.end()

            if len(loc) == len(query_strings):
                # We have seen all strings in query_strings, let's get to work.
                if res == (-1, -1) or idx - loc.front() < res[1] - res[0]:
                    res = (loc.front(), idx)
    return res
# @exclude


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


# O(n^2) solution
def check_ans(A, Q):
    d = set(Q)
    ans = (0, len(A) - 1)
    for l in range(len(A)):
        count = set()
        for r in range(l, len(A)):
            if r - l >= ans[1] - ans[0]:
                break
            if A[r] in d:
                count.add(A[r])
            if len(count) == len(Q):
                if r - l < ans[1] - ans[0]:
                    ans = (l, r)
                break
    return ans[1] - ans[0]


def simple_test_case(A, d, start, finish):
    res = find_smallest_subarray_covering_set(A, set(d))
    print('res =', *res)
    assert res == (start, finish)
    res = find_smallest_subarray_covering_subset(iter(A), d)
    print('res =', *res)
    assert res == (start, finish)


def simple_test():
    A = ['a', 'b', 'c', 'b', 'a', 'd', 'c', 'a', 'e', 'a', 'a', 'b', 'e']
    d = ['b', 'c', 'e']
    simple_test_case(A, d, 3, 8)
    d = ['a', 'c']
    simple_test_case(A, d, 6, 7)
    A = ['a', 'b']
    d = ['a', 'b']
    simple_test_case(A, d, 0, 1)
    A = ['a', 'b']
    d = ['b', 'a']
    simple_test_case(A, d, 0, 1)


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        A = [rand_string(random.randint(1, 10)) for i in range(n)]
        d = set(A)
        m = random.randint(1, len(d))
        Q = random.sample(d, m)
        inp = set(Q)
        res = find_smallest_subarray_covering_set(A, inp)
        print(*res, sep=', ')
        assert not inp.difference(A[res[0]:res[1]+1])
        res2 = find_smallest_subarray_covering_subset(iter(A), Q)
        print(*res2, sep=', ')
        assert not inp.difference(A[res[0]:res[1]+1])
        assert res[1] - res[0] == res2[1] - res2[0]
        assert res[1] - res[0] == check_ans(A, Q)


if __name__ == '__main__':
    main()
