# Online_sampling.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def online_sampling(n, k):
    H = {}
    for i in range(k):
        # Generate a random int in [0, n - 1 - i].
        b = n - 1 - i
        r = random.randint(0, b)
        r_mapped = H.get(r, r)  # value to which r is mapped
        b_mapped = H.get(b, b)  # value to which boundary n - 1 - i is mapped
        H[r] = b_mapped
        H[b] = r_mapped
    res = [H[n - 1 - i] for i in range(k)]
    return res
# @exclude


# Pythonic solution
def online_sampling_pythonic(n, k):
    return random.sample(range(n), k)


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = random.randint(1, n)
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        n = random.randint(1, 10000)
        k = random.randint(1, n)
    print('n =', n, 'k =', k)
    for _ in range(6):
        res = online_sampling(n, k)
        print('result =', *res)
        assert len(set(res)) == k
    print('result =', *online_sampling_pythonic(n, k))


if __name__ == '__main__':
    main()
