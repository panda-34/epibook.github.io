# Shortest_unique_prefix.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import collections
import random
import string


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


# @include
class TrieNode:
    def __init__(self):
        self.is_string = False
        self.leaves = collections.defaultdict(TrieNode)


class Trie:

    def __init__(self):
        self._root = TrieNode()

    def insert(self, s):
        p = self._root
        for c in s:
            p = p.leaves[c]

        # s already existed in this trie.
        if p.is_string:
            return False
        else:  # p.is_string == False.
            p.is_string = True  # Inserts s into this trie.
            return True

    def get_shortest_unique_prefix(self, s):
        p = self._root
        prefix = []
        for c in s:
            prefix.append(c)
            if c not in p.leaves:
                return ''.join(prefix)
            p = p.leaves[c]
        return ''


def find_shortest_prefix(s, D):
    # Builds a trie according to given dictionary D.
    T = Trie()
    for word in D:
        T.insert(word)
    return T.get_shortest_unique_prefix(s)
# @exclude


def check_ans(s, D):
    length = 0
    for it in D:
        for i in range(min(len(s), len(it))):
            if s[i] != it[i]:
                break
        else:
            i += 1
        if i > length:
            length = i
    if length == len(s):
        return ''
    else:
        return s[:length+1]


def main():
    for _ in range(100):
        if len(sys.argv) == 2:
            s = sys.argv[1]
        else:
            s = rand_string(random.randint(1, 10))
        n = random.randint(1, 10000)
        D = {rand_string(random.randint(1, 10)) for i in range(n)}
        print(s, 'prefix =', find_shortest_prefix(s, D))
        assert find_shortest_prefix(s, D) == check_ans(s, D)


if __name__ == '__main__':
    main()
