# Search_min_first_BST.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from binary_tree_prototype import BinaryTreeNode


# @include
def search_min_first_BST(min_first_BST, k):
    # First handle the base cases.
    if not min_first_BST or min_first_BST.data > k:
        return False
    elif min_first_BST.data == k:
        return True

    # Recursively search just the right subtree if the smallest key in the
    # right subtree is greater than or equal to k.
    if min_first_BST.right and k >= min_first_BST.right.data:
        return search_min_first_BST(min_first_BST.right, k)
    return search_min_first_BST(min_first_BST.left, k)
# @exclude


def main():
    # A min-first BST
    #      1
    #    2   4
    #  3    5 7
    tree = BinaryTreeNode(1)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(3)
    tree.right = BinaryTreeNode(4)
    tree.right.left = BinaryTreeNode(5)
    tree.right.right = BinaryTreeNode(7)
    assert search_min_first_BST(tree, 1)
    assert search_min_first_BST(tree, 3)
    assert search_min_first_BST(tree, 5)
    assert not search_min_first_BST(tree, 6)


if __name__ == '__main__':
    main()
