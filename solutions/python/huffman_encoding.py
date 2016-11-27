# Huffman_encoding.cc 884568f491146065472fafc32923e8aa73dd8076
import sys
import random
import heapq


k_english_freq = (
        8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966,
        0.153, 0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987,
        6.327, 9.056, 2.758, 0.978, 2.360,  0.150, 1.974, 0.074)


# @include
class CharWithFrequency:
    def __init__(self, c, freq):
        self.c = c
        self.freq = freq
# @exclude

    def __repr__(self):
        return '%r(%g)' % (self.c, self.freq)
# @include


class BinaryTreeNode:
    def __init__(self, aggregate_freq, s, left=None, right=None):
        self.aggregate_freq = aggregate_freq
        self.s = s
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.aggregate_freq <= other.aggregate_freq
# @exclude

    def symbols(self):
        return self.left.symbols() + self.right.symbols() if self.s is None else self.s.c

    def __repr__(self):
        return '%s <- %r(%g) -> %s' % (self.left and self.left.symbols(), self.symbols(),
                                       self.aggregate_freq, self.right and self.right.symbols())
# @include


def huffman_encoding(symbols):
    # Initially assigns each symbol into candidates.
    candidates = []
    for s in symbols:
        heapq.heappush(candidates, BinaryTreeNode(s.freq, s, ))

    # Keeps combining two nodes until there is one node left.
    while len(candidates) > 1:
        left = heapq.heappop(candidates)
        right = heapq.heappop(candidates)
        heapq.heappush(candidates, BinaryTreeNode(
            left.aggregate_freq + right.aggregate_freq, None, left, right))

    result = {}
    # Traverses the binary tree, assigning codes to nodes.
    assign_huffman_code(candidates[0], [], result)
    return result


def assign_huffman_code(tree, code, result):
    if tree:
        if tree.s:
            # This node is a leaf.
            result[tree.s.c] = ''.join(code)
        else:  # Non-leaf node.
            code.append('0')
            assign_huffman_code(tree.left, code, result)
            code[-1] = '1'
            assign_huffman_code(tree.right, code, result)
            del code[-1]
# @exclude


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] != 'huffman':
            n = int(sys.argv[1])
        else:
            n = 26
    else:
        n = random.randint(1, 255)
    symbols = []
    sum_ = 0
    if len(sys.argv) == 1 or sys.argv[1] != 'huffman':
        for i in range(n):
            t = CharWithFrequency(chr(i), random.randint(0, 100000))
            sum_ += t.freq
            symbols.append(t)
        for i in range(n):
            symbols[i].freq /= sum_
    else:
        for i in range(n):
            t = CharWithFrequency(chr(ord('a') + i), k_english_freq[i])
            symbols.append(t)
    result = huffman_encoding(symbols)
    avg = 0.0
    for symbol in symbols:
        print(symbol.c, symbol.freq, result[symbol.c])
        avg += symbol.freq / 100 * len(result[symbol.c])
    print('average huffman code length =', avg)


if __name__ == '__main__':
    main()
