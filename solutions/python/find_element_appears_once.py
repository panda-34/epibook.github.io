# Find_element_appears_once.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def find_element_appears_once(A):
    counts = [0] * 32
    for x in A:
        for i in range(32):
            if x & (1 << i):
                counts[i] += 1

    result = 0
    for i in range(32):
        result |= (counts[i] % 3) * (1 << i)
    return result
# @exclude


def find_element_appears_once_alternative(A):
    # ones denotes whether a bit-position has been set once (modulo 3) so far.
    # twos denotes whether a bit-position has been set twice (modulo 3) so far.
    ones = twos = 0
    for i in A:  # After reading A[i], bit-position j has a count of 1 modulo 3
        # if it had a count of 1 modulo 3 (the j-th bit in ones is set)
        # and the j-th bit in A[i] is 0 or the count was 0 modulo 3
        # (the j-th bit is not set in ones and in not set in twos) and
        # the j-th bit in A[i] is 1.
        next_ones = (~i & ones) | (i & ~ones & ~twos)

        # After reading A[i], bit-position j has a count of 2 modulo 3
        # if it had a count of 2 modulo 3 (the j-th bit in twos is set)
        # and the j-th bit in A[i] is a 0 or the count was 1 modulo 3
        # (the j-th bit is set in ones) and the j-th bit in A[i] is a 1.
        next_twos = (~i & twos) | (i & ones)

        ones = next_ones
        twos = next_twos

    # Since ones denotes bit-positions which have been set once (modulo 3),
    # it is the element which appears only once.
    return ones


def main():
    for _ in range(10000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        single = random.randrange(n)
        A = []
        for i in range(n):
            A.append(i)
            if i != single:
                A.append(i)
                A.append(i)
        print('Singleton element:', find_element_appears_once(A))
        assert find_element_appears_once(A) == single
        assert find_element_appears_once_alternative(A) == single


if __name__ == '__main__':
    main()
