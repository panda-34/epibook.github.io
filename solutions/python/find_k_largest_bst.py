# Find_k_largest_BST.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
from binary_tree_prototype import BinaryTreeNode


# @include
def find_k_largest_in_BST(tree, k):
    k_largest_elements = []
    find_k_largest_in_BST_helper(tree, k, k_largest_elements)
    return k_largest_elements


def find_k_largest_in_BST_helper(tree, k, k_largest_elements):
    # Perform reverse inorder traversal.
    if tree and len(k_largest_elements) < k:
        find_k_largest_in_BST_helper(tree.right, k, k_largest_elements)
        if len(k_largest_elements) < k:
            k_largest_elements.append(tree.data)
            find_k_largest_in_BST_helper(tree.left, k, k_largest_elements)
# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    if len(sys.argv) == 2:
        k = int(sys.argv[1])
    else:
        k = random.randint(1, 6)
    print('k =', k)
    ans = find_k_largest_in_BST(tree, k)
    print(*ans, sep='\n')
    for i in range(1, len(ans)):
        assert ans[i - 1] >= ans[i]
    ans = find_k_largest_in_BST(tree, 2)
    assert ans[0] == 6
    assert ans[1] == 5
    #      3
    #    3   4
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(3)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(4)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    ans = find_k_largest_in_BST(tree, 3)
    assert ans[0] == 6
    assert ans[1] == 4


if __name__ == '__main__':
    main()
