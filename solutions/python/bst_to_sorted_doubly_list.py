# BST_to_sorted_doubly_list.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import collections
from binary_tree_prototype import BinaryTreeNode


# @include
HeadAndTail = collections.namedtuple('HeadAndTail', ('head', 'tail'))


def BST_to_doubly_linked_list(tree):
    return BST_to_doubly_linked_list_helper(tree).head


# Transforms a BST into a sorted doubly linked list in-place,
# and return the head and tail of the list.
def BST_to_doubly_linked_list_helper(tree):
    # Empty subtree.
    if not tree:
        return HeadAndTail(None, None)

    # Recursively builds the list from left and right subtrees.
    left = BST_to_doubly_linked_list_helper(tree.left)
    right = BST_to_doubly_linked_list_helper(tree.right)

    # Appends tree to the list from left subtree.
    if left.tail:
        left.tail.right = tree
    tree.left = left.tail

    # Appends the list from right subtree to tree.
    tree.right = right.head
    if right.head:
        right.head.left = tree

    return HeadAndTail(left.head or tree, right.tail or tree)
# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    root = BinaryTreeNode(3)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(4)
    root.right.right = BinaryTreeNode(6)
    L = BST_to_doubly_linked_list(root)
    curr = L
    pre = float('-inf')
    while curr:
        assert pre <= curr.data
        print(curr.data)
        pre = curr.data
        curr = curr.right


if __name__ == '__main__':
    main()
