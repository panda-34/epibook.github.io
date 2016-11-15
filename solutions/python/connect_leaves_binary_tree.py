# Connect_leaves_binary_tree.cpp 100b4adabfd008775520062bd407c3323ea646af
from binary_tree_prototype import BinaryTreeNode


# @include
def create_list_of_leaves(tree):
    leaves = []
    if tree:
        if not tree.left and not tree.right:
            leaves.append(tree)
        else:
            # First do the left subtree, and then do the right subtree.
            leaves += create_list_of_leaves(tree.left)
            leaves += create_list_of_leaves(tree.right)
    return leaves


# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    L = create_list_of_leaves(tree)
    assert len(L) == 1 and L[0].data == 2

    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    L = create_list_of_leaves(tree)
    output = []
    # should output 1, 4, 6
    for l in L:
        output.append(l.data)
        print(l.data)
    golden_res = [1, 4, 6]
    assert output == golden_res


if __name__ == '__main__':
    main()
