# Rebuild_BST_preorder_better.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from binary_tree_prototype import BinaryTreeNode


# @include
def rebuild_BST_from_preorder(preorder_sequence):
    root_idx = 0
    return rebuild_BST_from_preorder_on_value_range(preorder_sequence,
                                                    float('-inf'),
                                                    float('inf'), root_idx)[0]


# Builds a BST on the subtree rooted at root_idx from preorder_sequence on
# keys in (lower_bound, upper_bound).
def rebuild_BST_from_preorder_on_value_range(preorder_sequence, lower_bound,
                                             upper_bound, root_idx):
    if root_idx == len(preorder_sequence):
        return None, root_idx

    root = preorder_sequence[root_idx]
    if root < lower_bound or root > upper_bound:
        return None, root_idx
    root_idx += 1
    # Note that rebuild_BST_from_preorder_on_value_range updates root_idx. So the
    # order of following two calls are critical.
    left_subtree, root_idx = rebuild_BST_from_preorder_on_value_range(
        preorder_sequence, lower_bound, root, root_idx)
    right_subtree, root_idx = rebuild_BST_from_preorder_on_value_range(
        preorder_sequence, root, upper_bound, root_idx)
    return BinaryTreeNode(root, left_subtree, right_subtree), root_idx


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
