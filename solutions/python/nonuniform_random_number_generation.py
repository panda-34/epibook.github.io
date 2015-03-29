# nonuniform_random_number_generation.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
import collections
import itertools
import bisect


# @include
def nonuniform_random_number_generation(T, P):
    prefix_P = [0.0]
    prefix_P += itertools.accumulate(P)
    it = bisect.bisect(prefix_P, random.random())
    return T[it - 1]
# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 50)
    T = [float(i) for i in range(n)]
    P = []
    full_prob = 1.0
    for i in range(n - 1):
        pi = random.uniform(0.0, full_prob)
        P.append(pi)
        full_prob -= pi
    P.append(full_prob)
    print(*T)
    print(*P)
    print(nonuniform_random_number_generation(T, P))
    # Test. Perform the nonuniform random number generation for n * k_times times
    # and calculate the distribution of each bucket.
    k_times = 100000
    counts = collections.Counter(
        int(nonuniform_random_number_generation(T, P)) for i in range(n * k_times))
    for i in range(n):
        print(counts[i] / (n * k_times), P[i])
        assert abs(counts[i] / (n * k_times) - P[i]) < 0.01


if __name__ == '__main__':
    main()
