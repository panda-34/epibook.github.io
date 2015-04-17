# sum-root-to-leaf-binary-tree.cc 100b4adabfd008775520062bd407c3323ea646af
from binary_tree_prototype import BinaryTreeNode


# @include
def sum_root_to_leaf(tree):
    return sum_root_to_leaf_helper(tree, 0)


def sum_root_to_leaf_helper(tree, partial_path_sum):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:  # Leaf.
        return partial_path_sum
    # Non-leaf.
    return (sum_root_to_leaf_helper(tree.left, partial_path_sum) +
            sum_root_to_leaf_helper(tree.right, partial_path_sum))
# @exclude


def main():
    #      1
    #    1   0
    #  0    1 0
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(1)
    root.left.left = BinaryTreeNode(0)
    root.right = BinaryTreeNode(0)
    root.right.left = BinaryTreeNode(1)
    root.right.right = BinaryTreeNode(0)
    result = sum_root_to_leaf(root)
    assert result == 15


if __name__ == '__main__':
    main()
