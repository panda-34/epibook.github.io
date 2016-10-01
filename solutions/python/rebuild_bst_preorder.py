# Rebuild_BST_preorder.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from binary_tree_prototype import BinaryTreeNode


# @include
def rebuild_BST_from_preorder(preorder_sequence):
    return rebuild_BST_from_preorder_helper(preorder_sequence, 0, len(preorder_sequence))


# Builds a BST from preorder_sequence[start : end - 1].
def rebuild_BST_from_preorder_helper(preorder_sequence, start, end):
    if start >= end:
        return None
    transition_point = start + 1
    while (transition_point < end and
           preorder_sequence[transition_point] < preorder_sequence[start]):
        transition_point += 1

    return BinaryTreeNode(preorder_sequence[start],
        rebuild_BST_from_preorder_helper(preorder_sequence, start + 1, transition_point),
        rebuild_BST_from_preorder_helper(preorder_sequence, transition_point, end))
# @exclude


def check_ans(n, pre):
    if n:
        check_ans(n.left, pre)
        assert pre <= n.data
        print(n.data)
        check_ans(n.right, n.data)


def main():
    #      3
    #    2   5
    #  1    4 6
    # should output 1, 2, 3, 4, 5, 6
    # preorder [3, 2, 1, 5, 4, 6]
    preorder = [3, 2, 1, 5, 4, 6]
    tree = rebuild_BST_from_preorder(preorder)
    check_ans(tree, float('-inf'))
    assert 3 == tree.data
    assert 2 == tree.left.data
    assert 1 == tree.left.left.data
    assert 5 == tree.right.data
    assert 4 == tree.right.left.data
    assert 6 == tree.right.right.data


if __name__ == '__main__':
    main()
