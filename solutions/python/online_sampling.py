# Online_sampling.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def online_sampling(n, k):
    changed_elements = {}
    for i in range(k):
        # Generate a random index in [i, n - 1].
        rand_idx = random.randrange(i, n)
        rand_idx_mapped, i_mapped = changed_elements.get(
            rand_idx, rand_idx), changed_elements.get(i, i)
        changed_elements[rand_idx], changed_elements[
            i] = i_mapped, rand_idx_mapped
    return [changed_elements[i] for i in range(k)]
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
