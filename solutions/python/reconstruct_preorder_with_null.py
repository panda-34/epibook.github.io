# Reconstruct_preorder_with_null.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
import random
from binary_tree_prototype import BinaryTreeNode
from binary_tree_utils import generate_rand_binary_tree, is_two_binary_trees_equal


# @include
def reconstruct_preorder(preorder):
    return reconstruct_preorder_helper(iter(preorder))


def reconstruct_preorder_helper(it_preorder):
    subtree_key = next(it_preorder)
    if subtree_key is None:
        return None

    # Note that reconstruct_preorder_helper updates it_preorder. So the order of
    # following two calls are critical.
    left_subtree = reconstruct_preorder_helper(it_preorder)
    right_subtree = reconstruct_preorder_helper(it_preorder)
    return BinaryTreeNode(subtree_key, left_subtree, right_subtree)
# @exclude


def gen_preorder_with_null(n, p):
    if not n:
        p.append(None)
        return

    p.append(n.data)
    gen_preorder_with_null(n.left, p)
    gen_preorder_with_null(n.right, p)


def main():
    for times in range(1000):
        print(times)
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 10000)
        root = generate_rand_binary_tree(n)
        p = []
        gen_preorder_with_null(root, p)
        x = reconstruct_preorder(p)
        assert is_two_binary_trees_equal(root, x)


if __name__ == '__main__':
    main()
