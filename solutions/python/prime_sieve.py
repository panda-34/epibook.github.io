# Prime_sieve.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
# Given n, return the primes from 1 to n.
def generate_primes_from_1_to_n(n):
    size = (n - 3) // 2 + 1
    primes = [2]  # Stores the primes from 1 to n.
    # is_prime[i] represents (2i + 3) is prime or not. Initially assuming
    # everyone is prime (by setting as True).
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # Sieving from p^2, where p^2 = 4i^2 + 12i + 9 whose index in is_prime
            # is 2i^2 + 6i + 3 because is_prime[i] represents 2i + 3.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes
# @exclude


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        print('n =', n)
        primes = generate_primes_from_1_to_n(n)
        print(*primes, sep='\n')
        for i in primes:
            for j in range(2, i):
                assert i % j
    else:
        for _ in range(100):
            n = random.randint(2, 100000)
            print('n =', n)
            primes = generate_primes_from_1_to_n(n)
            for i in primes:
                for j in range(2, i):
                    assert i % j


if __name__ == '__main__':
    main()
