# Online_median.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import heapq


# @include
def online_median(sequence):
    # min_heap stores the larger half seen so far.
    min_heap = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative
    max_heap = []

    for x in sequence:
        if min_heap and x < min_heap[0]:
            heapq.heappush(max_heap, -x)
        else:
            heapq.heappush(min_heap, x)

        if len(min_heap) > len(max_heap) + 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(min_heap) == len(max_heap):
            print(0.5 * (min_heap[0] + (-max_heap[0])))
        else:
            print(min_heap[0] if len(min_heap) > len(max_heap) else -max_heap[0])
# @exclude


def main():
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
    else:
        num = random.randint(1, 100000)
    stream = [random.randint(1, 10000) for i in range(num)]
    print(*stream, sep='\n')
    print()
    online_median(iter(stream))


if __name__ == '__main__':
    main()
