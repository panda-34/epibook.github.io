# unique-binary-trees-all.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
from binary_tree_prototype import BinaryTreeNode


# @include
def generate_all_binary_trees(num_nodes):
    result = []
    if num_nodes == 0:  # Empty tree, add as a None.
        result.append(None)

    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)
        # Generates all combinations of left_subtrees and right_subtrees.
        for left in left_subtrees:
            for right in right_subtrees:
                result.append(BinaryTreeNode(0, clone(left), clone(right)))
    return result


def clone(tree):
    if not tree:
        return None
    return BinaryTreeNode(tree.data, clone(tree.left), clone(tree.right))


# @exclude


def small_test():
    assert len(generate_all_binary_trees(1)) == 1
    assert len(generate_all_binary_trees(2)) == 2
    assert len(generate_all_binary_trees(3)) == 5
    assert len(generate_all_binary_trees(4)) == 14
    assert len(generate_all_binary_trees(5)) == 42
    assert len(generate_all_binary_trees(10)) == 16796


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10)
    print('n =', n)
    generate_all_binary_trees(n)


if __name__ == '__main__':
    main()
