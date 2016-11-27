# Search_frequent_items.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string
import collections


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


# @include
# Finds the candidates which may occur > n / k times.
def search_frequent_items(k, sin):
    hash = collections.Counter()
    n = 0  # Count the number of strings.

    for buf in sin:
        hash[buf] += 1
        n += 1
        # Detecting k items in hash, at least one of them must have exactly
        # one in it. We will discard those k items by one for each.
        if len(hash) == k:
            for it in hash:
                hash[it] -= 1
            hash = +hash  # remove all zero values

    # Resets hash for the following counting.
    for it in hash:
        hash[it] = 0

    # Resets the stream and read it again.
    # Counts the occurrence of each candidate word.
    for buf in sin:
        if buf in hash:
            hash[buf] += 1

    # Selects the word which occurs > n / k times.
    ret = [it for it, value in hash.items() if value > n / k]
    return ret
# @exclude


def check_ans(stream, k, items):
    items.sort()
    stream.sort()
    count = 1
    idx = 0
    for i in range(1, len(stream)):
        if stream[i] != stream[i - 1]:
            if count > len(stream) / k:
                assert idx < len(items)
                assert stream[i - 1] == items[idx]
                idx += 1
            count = 1
        else:
            count += 1
    if count > len(stream) / k:
        assert stream[-1] == items[idx]
        idx += 1
    assert idx == len(items)


def main():
    for times in range(1000):
        print(times)
        stream = []
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
            k = random.randint(1, n)
        elif len(sys.argv) == 3:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
        else:
            n = random.randrange(100000)
            k = random.randint(1, n)
        stream = [rand_string(random.randint(1, 5)) for i in range(n)]
        items = search_frequent_items(k, stream)
        check_ans(stream, k, items)


if __name__ == '__main__':
    main()
