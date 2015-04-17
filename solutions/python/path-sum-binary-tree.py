# path-sum-binary-tree.cc 100b4adabfd008775520062bd407c3323ea646af
from binary_tree_prototype import BinaryTreeNode


# @include
def has_path_sum(tree, target_sum):
    return has_path_sum_helper(tree, 0, target_sum)


def has_path_sum_helper(node, partial_path_sum, target_sum):
    if not node:
        return False
    partial_path_sum += node.data
    if not node.left and not node.right:  # Leaf.
        return partial_path_sum == target_sum
    # Non-leaf.
    return (has_path_sum_helper(node.left, partial_path_sum, target_sum) or
            has_path_sum_helper(node.right, partial_path_sum, target_sum))
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
    assert has_path_sum(tree, 6)
    assert not has_path_sum(tree, 7)
    assert not has_path_sum(tree, 100)


if __name__ == '__main__':
    main()
