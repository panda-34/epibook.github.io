# Successor.cpp b4b3a70d8ab942579f85b4416f980d05831af969
from binary_tree_with_parent_prototype import BinaryTreeNode


# @include
def find_successor(node):
    it = node
    if it.right:
        # Successor is the leftmost element in node's right subtree.
        it = it.right
        while it.left:
            it = it.left
        return it

    # Find the closest ancestor whose left subtree contains node.
    while it.parent and it.parent.right is it:
        it = it.parent

    # A return value of None means node does not have successor, i.e., it is
    # the rightmost node in the tree.
    return it.parent
# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    root = BinaryTreeNode(3)
    root.parent = None
    root.left = BinaryTreeNode(2)
    root.left.parent = root
    root.left.left = BinaryTreeNode(1)
    root.left.left.parent = root.left
    root.right = BinaryTreeNode(5)
    root.right.parent = root
    root.right.left = BinaryTreeNode(4)
    root.right.left.parent = root.right
    root.right.right = BinaryTreeNode(6)
    root.right.right.parent = root.right
    # should output 6
    node = find_successor(root.right)
    assert 6 == node.data
    if node:
        print(node.data)
    else:
        print('null')
    # should output 'null'
    node = find_successor(root.right.right)
    assert not node
    if node:
        print(node.data)
    else:
        print('null')


if __name__ == '__main__':
    main()
