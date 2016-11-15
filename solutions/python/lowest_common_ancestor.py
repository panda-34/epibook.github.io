# Lowest_common_ancestor.cpp b4b3a70d8ab942579f85b4416f980d05831af969
from binary_tree_with_parent_prototype import BinaryTreeNode


# @include
def LCA(node_0, node_1):
    depth_0 = get_depth(node_0)
    depth_1 = get_depth(node_1)
    # Makes node_0 as the deeper node in order to simplify the code.
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0

    # Ascends from the deeper node.
    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        node_0 = node_0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA.
    while node_0 is not node_1:
        node_0 = node_0.parent
        node_1 = node_1.parent
    return node_0


def get_depth(node):
    depth = 0
    while node:
        depth += 1
        node = node.parent
    return depth


# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    root = BinaryTreeNode(3, None, None, None)
    root.left = BinaryTreeNode(2, None, None, root)
    root.left.left = BinaryTreeNode(1, None, None, root.left)
    root.right = BinaryTreeNode(5, None, None, root)
    root.right.left = BinaryTreeNode(4, None, None, root.right)
    root.right.right = BinaryTreeNode(6, None, None, root.right)

    # should output 3
    assert LCA(root.left, root.right).data == 3
    print(LCA(root.left, root.right).data)
    # should output 5
    assert LCA(root.right.left, root.right.right).data == 5
    print(LCA(root.right.left, root.right.right).data)
    # should output 3
    assert LCA(root.left, root.right.left).data == 3
    print(LCA(root.left, root.right.left).data)
    # should output 2
    assert LCA(root.left, root.left.left).data == 2
    print(LCA(root.left, root.left.left).data)


if __name__ == '__main__':
    main()
