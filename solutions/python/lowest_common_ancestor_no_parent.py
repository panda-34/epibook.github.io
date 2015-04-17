# Lowest_common_ancestor_no_parent.cpp 100b4adabfd008775520062bd407c3323ea646af
from binary_tree_prototype import BinaryTreeNode


# @include
def LCA(tree, node0, node1):
    return LCAHelper(tree, node0, node1)[1]


# Returns a pair of int and node pointer; int field is 0, 1, or 2 depending
# on how many of node0 and node1 are present in tree. If both are present in
# tree, the node pointer is a common ancestor. It may not be the LCA
# initially, but it will be LCA when the algorithm terminates.
def LCAHelper(tree, node0, node1):
    if not tree:
        return (0, None)

    left_result = LCAHelper(tree.left, node0, node1)
    if left_result[0] == 2:  # Found both nodes in the left subtree.
        return left_result
    right_result = LCAHelper(tree.right, node0, node1)
    if right_result[0] == 2:  # Found both nodes in the right subtree.
        return right_result
    num_target_nodes = (left_result[0] + right_result[0] +
                        (tree is node0 or tree is node1))
    return (num_target_nodes, tree if num_target_nodes == 2 else None)
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
    # should output 3
    x = LCA(tree, tree.left, tree.right)
    assert x.data == 3
    print(x.data)
    # should output 5
    x = LCA(tree, tree.right.left, tree.right.right)
    assert x.data == 5
    print(x.data)
    # should output 5
    x = LCA(tree, tree.right, tree.right.right)
    assert x.data == 5
    print(x.data)
    # should output 3
    x = LCA(tree, tree, tree.left.left)
    assert x.data == 3
    print(x.data)
    # should output 2
    x = LCA(tree, tree.left, tree.left.left)
    assert x.data == 2
    print(x.data)


if __name__ == '__main__':
    main()
