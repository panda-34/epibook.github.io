# BST_lowest_common_ancestor.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from binary_tree_prototype import BinaryTreeNode


# @include
# Input nodes are not nonempty and the key at s is less than or equal to that at b.
def find_LCA(tree, s, b):
    p = tree
    while p.data < s.data or p.data > b.data:
        # Keep searching since p is outside of [s, b].
        while p.data < s.data:
            p = p.right  # LCA must be in p's right child.
        while p.data > b.data:
            p = p.left  # LCA must be in p's left child.
    # Now, s->data <= p->data && p->data <= b->data.
    return p


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
    assert 3 == find_LCA(tree, tree.left.left, tree.right.left).data
    assert 5 == find_LCA(tree, tree.right.left, tree.right.right).data
    assert 2 == find_LCA(tree, tree.left.left, tree.left).data


if __name__ == '__main__':
    main()
