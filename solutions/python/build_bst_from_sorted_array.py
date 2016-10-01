# Build_BST_from_sorted_array.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
from binary_tree_prototype import BinaryTreeNode


# @include
def build_min_height_BST_from_sorted_array(A):
    return build_min_height_BST_from_sorted_array_helper(A, 0, len(A))


# Build a min-height BST over the entries in A[start : end - 1].
def build_min_height_BST_from_sorted_array_helper(A, start, end):
    if start >= end:
        return None
    mid = start + ((end - start) // 2)
    return BinaryTreeNode(A[mid],
                          build_min_height_BST_from_sorted_array_helper(A, start, mid),
                          build_min_height_BST_from_sorted_array_helper(A, mid + 1, end))
# @exclude


def traversal_check(tree, target):
    if tree:
        target = traversal_check(tree.left, target)
        assert target == tree.data
        target += 1
        target = traversal_check(tree.right, target)
    return target


def simple_test():
    A = [1, 2, 3, 4]
    result = build_min_height_BST_from_sorted_array(A)
    assert 3 == result.data
    assert 2 == result.left.data
    assert 1 == result.left.left.data
    assert 4 == result.right.data


def main():
    simple_test()
    for _ in range(1000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 1000)
        A = list(range(n))
        tree = build_min_height_BST_from_sorted_array(A)
        target = 0
        traversal_check(tree, target)


if __name__ == '__main__':
    main()
