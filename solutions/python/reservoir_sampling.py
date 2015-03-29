# Reservoir_sampling.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import itertools


# @include
def reservoir_sampling(it, k):
    # Stores the first k elements.
    sampling_results = list(itertools.islice(it, k))

    # After the first k elements.
    element_num = k
    for x in it:
        # Generate a random int in [0, element_num].
        element_num += 1
        tar = random.randrange(element_num)
        if tar < k:
            sampling_results[tar] = x
    return sampling_results
# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = random.randint(1, n)
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        n = random.randint(1, 99999)
        k = random.randint(1, n)
    print(n, k)
    A = range(n)
    ans = reservoir_sampling(iter(A), k)
    assert len(ans) == k
    #print(*ans)


if __name__ == '__main__':
    main()
