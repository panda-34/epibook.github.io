# Nearest_repetition.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


# @include
def find_nearest_repetition(paragraph):
    word_to_latest_index = {}
    nearest_repeated_distance = float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word)
        word_to_latest_index[word] = i
    return nearest_repeated_distance
# @exclude


# O(n^2) checking
def check_answer(s):
    nearest_repeated_distance = float('inf')
    for i, word in enumerate(s):
        for j in range(i + 1, len(s)):
            if word == s[j]:
                nearest_repeated_distance = min(nearest_repeated_distance, j - i)
    return nearest_repeated_distance


def main():
    A = ['foo', 'bar', 'widget', 'foo', 'widget', 'widget', 'adnan']
    assert check_answer(A) == find_nearest_repetition(A)
    A = ['foo', 'bar', 'widget', 'foo', 'xyz', 'widget', 'bar', 'adnan']
    assert check_answer(A) == find_nearest_repetition(A)
    A = ['foo', 'bar', 'widget', 'adnan']
    assert check_answer(A) == find_nearest_repetition(A)
    A = []
    assert check_answer(A) == find_nearest_repetition(A)
    A = ['foo', 'foo', 'foo']
    assert check_answer(A) == find_nearest_repetition(A)
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        s = [rand_string(random.randint(1, 10)) for i in range(n)]
        assert check_answer(s) == find_nearest_repetition(s)


if __name__ == '__main__':
    main()
