import collections
import sys
import random
import heapq


# @include
def top_k(k, stream):
    min_heap = []
    for next_string in stream:
        heapq.heappush(min_heap, (len(next_string), next_string))
        # Remove the shortest string. Note that the comparison function will order the strings by length.
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [p[1] for p in min_heap]


# @exclude


def main():
    for _ in range(1000):
        num = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 10)
        A = [str(random.randint(1, 10000000)) for i in range(num)]
        k = random.randint(1, num)
        sin = iter(A)
        result = top_k(k, sin)
        A = sorted(A, key=lambda s: len(s))
        assert collections.Counter(
            [len(a) for a in result]) == collections.Counter(
                [len(a) for a in A[-k:]])


if __name__ == '__main__':
    main()
