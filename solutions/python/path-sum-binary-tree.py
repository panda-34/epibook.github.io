# path-sum-binary-tree.cc 100b4adabfd008775520062bd407c3323ea646af
from binary_tree_prototype import BinaryTreeNode


# @include
def has_path_sum(tree, target_sum, partial_path_sum=0):
    if not tree:
        return False
    partial_path_sum += tree.data
    if not tree.left and not tree.right:  # Leaf.
        return partial_path_sum == target_sum
    # Non-leaf.
    return has_path_sum(tree.left, target_sum,
                        partial_path_sum) or has_path_sum(
                            tree.right, target_sum, partial_path_sum)


# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    assert has_path_sum(tree, 3)
    tree.left = BinaryTreeNode(2)
    assert has_path_sum(tree, 5)
    tree.left.left = BinaryTreeNode(1)
    assert has_path_sum(tree, 6)
    tree.right = BinaryTreeNode(5)
    assert has_path_sum(tree, 8)
    assert not has_path_sum(tree, 7)
    tree.right.left = BinaryTreeNode(4)
    assert has_path_sum(tree, 12)
    assert not has_path_sum(tree, 1)
    assert not has_path_sum(tree, 3)
    assert not has_path_sum(tree, 5)
    tree.right.right = BinaryTreeNode(6)
    assert has_path_sum(tree, 6)
    assert not has_path_sum(tree, 7)
    assert has_path_sum(tree, 14)
    assert not has_path_sum(tree, -1)
    assert not has_path_sum(tree, 2**64 - 1)
    assert not has_path_sum(tree, -2**64)


if __name__ == '__main__':
    main()
