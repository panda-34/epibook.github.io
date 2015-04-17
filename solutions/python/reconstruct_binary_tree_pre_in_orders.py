# Reconstruct_binary_tree_pre_in_orders.cpp 100b4adabfd008775520062bd407c3323ea646af
import sys
import random
from binary_tree_prototype import BinaryTreeNode
from binary_tree_utils import generate_rand_binary_tree, generate_preorder, generate_inorder, is_two_binary_trees_equal


# @include
def binary_tree_from_preorder_inorder(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
    return binary_tree_from_preorder_inorder_helper(preorder, 0, len(preorder),
                                                    0, len(inorder),
                                                    node_to_inorder_idx)


# Builds the subtree with preorder[preorder_start : preorder_end - 1] and
# inorder[inorder_start : inorder_end - 1].
def binary_tree_from_preorder_inorder_helper(preorder, preorder_start, preorder_end,
                                             inorder_start, inorder_end,
                                             node_to_inorder_idx):
    if preorder_end <= preorder_start or inorder_end <= inorder_start:
        return None

    root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
    left_subtree_size = root_inorder_idx - inorder_start

    return BinaryTreeNode(
        preorder[preorder_start],
        # Recursively builds the left subtree.
        binary_tree_from_preorder_inorder_helper(
            preorder, preorder_start + 1, preorder_start + 1 + left_subtree_size,
            inorder_start, root_inorder_idx, node_to_inorder_idx),
        # Recursively builds the right subtree.
        binary_tree_from_preorder_inorder_helper(
            preorder, preorder_start + 1 + left_subtree_size, preorder_end,
            root_inorder_idx + 1, inorder_end, node_to_inorder_idx))
# @exclude


def main():
    for times in range(1000):
        print(times)
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        root = generate_rand_binary_tree(n, True)
        pre_order = generate_preorder(root)
        in_order = generate_inorder(root)
        res = binary_tree_from_preorder_inorder(pre_order, in_order)
        assert is_two_binary_trees_equal(root, res)


if __name__ == '__main__':
    main()
