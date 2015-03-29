# Offline_sampling.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def offline_sampling(A, k):
    for i in range(k):
        # Generate a random int in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    del A[k:]
    return A
# @exclude


# Pythonic solution
def offline_sampling_pythonic(A, k):
    return random.sample(A, k)


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        k = random.randint(1, n)
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
    else:
        n = random.randint(1, 1000000)
        k = random.randint(1, n)

    A = list(range(n))
    print(n, k)
    ans = offline_sampling(A, k)
    assert len(ans) == k
    print(*ans)
    print(*offline_sampling_pythonic(list(range(n)), k))


if __name__ == '__main__':
    main()
