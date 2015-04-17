# BST_sorted_order.cpp dd7adc0dbf96e35e29defe6d31337c155c450a2f
from bst_prototype import BSTNode


result = []


# @include
def print_BST_in_sorted_order(tree):
    s = []
    curr = tree

    while s or curr:
        if curr:
            s.append(curr)
            # Going left.
            curr = curr.left
        else:
            # Going up.
            curr = s.pop()
            print(curr.data)
            # @exclude
            result.append(curr.data)
            # @include
            # Going right.
            curr = curr.right
# @exclude


def main():
    #        43
    #    23     47
    #      37      53
    #    29  41
    #     31
    tree = BSTNode(43)
    tree.left = BSTNode(23)
    tree.left.right = BSTNode(37)
    tree.left.right.left = BSTNode(29)
    tree.left.right.left.right = BSTNode(31)
    tree.left.right.right = BSTNode(41)
    tree.right = BSTNode(47)
    tree.right.right = BSTNode(53)
    print_BST_in_sorted_order(tree)
    golden_res = [23, 29, 31, 37, 41, 43, 47, 53]
    assert golden_res == result


if __name__ == '__main__':
    main()
