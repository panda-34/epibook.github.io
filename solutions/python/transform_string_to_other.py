# Transform_string_to_other.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string
import collections


def rand_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


# @include
# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    StringWithDistance = collections.namedtuple('StringWithDistance', (
        'candidate_string', 'distance'))
    q = collections.deque()
    D.remove(s)  # Marks s as visited by erasing it in D.
    q.append(StringWithDistance(s, 0))

    while q:
        f = q.popleft()
        # Returns if we find a match.
        if f.candidate_string == t:
            return f.distance  # Number of steps reaches t.

        # Tries all possible transformations of f.candidate_string.
        for i in range(len(f.candidate_string)):
            for j in string.ascii_lowercase:  # Iterates through 'a' ~ 'z'.
                cand = f.candidate_string[:i] + j + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1  # Cannot find a possible transformations.


# @exclude


def main():
    if len(sys.argv) == 2:
        length = int(sys.argv[1])
    else:
        length = random.randint(1, 10)
    s = rand_string(length)
    t = rand_string(length)
    D = {s, t}
    n = random.randint(1, 1000000)
    for i in range(n):
        D.add(rand_string(length))
    print(s, t, len(D))
    print(transform_string(D, s, t))


if __name__ == '__main__':
    main()
