# Minimum_distance_3_sorted_arrays.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import operator
import itertools
import random
import sortedcontainers


# @include
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    min_distance_so_far = float('inf')
    # Stores array iterators in each entry.
    iters = sortedcontainers.SortedList(key=operator.itemgetter(0))
    for sorted_array in sorted_arrays:
        it = iter(sorted_array)
        next(it)
        iters.add((sorted_array[0], it))

    while True:
        min_value = iters[0][0]
        max_value = iters[-1][0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters[0][1]
        next_min = next(it, None)
        # Return if some array has no remaining elements.
        if next_min is None:
            return min_distance_so_far
        iters.add((next_min, it))
        del iters[0]


# @exclude


def brute_force_gen_answer(sorted_arrays):
    ans = min(
        max(values) - min(values)
        for values in itertools.product(*sorted_arrays))
    print(ans)
    return ans


def main():
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 5)
        sorted_arrays = []
        for i in range(n):
            size = random.randint(1, 40)
            sorted_arrays.append(
                sorted(random.randrange(10000) for i in range(size)))
        ans = find_closest_elements_in_sorted_arrays(sorted_arrays)
        print(ans)
        assert brute_force_gen_answer(sorted_arrays) == ans


if __name__ == '__main__':
    main()
