# Exterior_binary_tree.cpp 100b4adabfd008775520062bd407c3323ea646af
from binary_tree_prototype import BinaryTreeNode

# @include
def exterior_binary_tree(tree):
    exterior = []
    if tree:
        exterior.append(tree)
        exterior += left_boundary_and_leaves(tree.left, True)
        exterior += right_boundary_and_leaves(tree.right, True)
    return exterior


# Computes the nodes from the root to the leftmost leaf followed by all the
# leaves in subtree.
def left_boundary_and_leaves(subtree, is_boundary):
    result = []
    if subtree:
        if is_boundary or is_leaf(subtree):
            result.append(subtree)
        result += left_boundary_and_leaves(subtree.left, is_boundary)
        result += left_boundary_and_leaves(subtree.right,
                                           is_boundary and not subtree.left)
    return result


# Computes the leaves in left-to-right order followed by the rightmost leaf
# to the root path in subtree.
def right_boundary_and_leaves(subtree, is_boundary):
    result = []
    if subtree:
        result += right_boundary_and_leaves(subtree.left,
                                            is_boundary and not subtree.right)
        result += right_boundary_and_leaves(subtree.right, is_boundary)
        if is_boundary or is_leaf(subtree):
            result.append(subtree)
    return result


def is_leaf(node):
    return not node.left and not node.right
# @exclude


def main():
    #        3
    #    2      5
    #  1  0    4 6
    #   -1 -2
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.right = BinaryTreeNode(0)
    tree.left.right.left = BinaryTreeNode(-1)
    tree.left.right.right = BinaryTreeNode(-2)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    golden_res = [3, 2, 1, -1, -2, 4, 6, 5]
    L = exterior_binary_tree(tree)
    output = []
    # should output 3 2 1 -1 -2 4 6 5
    for l in L:
        output.append(l.data)
        print(l.data)
    assert output == golden_res


if __name__ == '__main__':
    main()
