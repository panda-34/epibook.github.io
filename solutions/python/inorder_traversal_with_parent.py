# Inorder_traversal_with_parent.cpp b4b3a70d8ab942579f85b4416f980d05831af969
from binary_tree_with_parent_prototype import BinaryTreeNode


result = []


# @include
def inorder_traversal(tree):
    prev = None
    curr = tree
    while curr:
        if prev is curr.parent:
            # We came down to curr from prev.
            if curr.left:  # Keep going left.
                nxt = curr.left
            else:
                print(curr.data)
                # @exclude
                result.append(curr.data)
                # @include
                # Done with left, so go right if right is not empty.
                # Otherwise, go up.
                nxt = curr.right or curr.parent
        elif curr.left is prev:
            # We came up to curr from its left child.
            print(curr.data)
            # @exclude
            result.append(curr.data)
            # @include
            # Done with left, so go right if right is not empty. Otherwise, go up.
            nxt = curr.right or curr.parent
        else:  # Done with both children, so move up.
            nxt = curr.parent

        prev = curr
        curr = nxt
# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    root = BinaryTreeNode(3)
    root.parent = None
    root.left = BinaryTreeNode(2)
    root.left.parent = root
    root.left.left = BinaryTreeNode(1)
    root.left.left.parent = root.left
    root.right = BinaryTreeNode(5)
    root.right.parent = root
    root.right.left = BinaryTreeNode(4)
    root.right.left.parent = root.right
    root.right.right = BinaryTreeNode(6)
    root.right.right.parent = root.right

    # Should output 1 2 3 4 5 6.
    inorder_traversal(root)
    golden_res = [1, 2, 3, 4, 5, 6]
    assert golden_res == result


if __name__ == '__main__':
    main()
