# reconstruct-almost-bst.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from binary_tree_prototype import BinaryTreeNode
from binary_tree_utils import generate_inorder


# @include
class Inversion:

    def __init__(self, prev=None, next=None):
        self.prev = prev
        self.next = next


def reconstruct_BST(almost_BST):
    inversion_0 = Inversion()
    inversion_1 = Inversion()
    prev = None
    reconstruct_BST_helper(almost_BST, inversion_0, inversion_1, prev)
    if inversion_1.next:  # Swaps the out of order nodes.
        inversion_0.prev.data, inversion_1.next.data = inversion_1.next.data, inversion_0.prev.data
    else:
        inversion_0.prev.data, inversion_0.next.data = inversion_0.next.data, inversion_0.prev.data


def reconstruct_BST_helper(almost_BST, inversion_0, inversion_1, prev):
    if almost_BST is None:
        return prev

    prev = reconstruct_BST_helper(almost_BST.left, inversion_0, inversion_1, prev)
    if prev and prev.data > almost_BST.data:
        # Inversion detected.
        if inversion_0.prev is None and inversion_0.next is None:
            inversion_0.prev = prev
            inversion_0.next = almost_BST
        else:
            inversion_1.prev = prev
            inversion_1.next = almost_BST
    prev = almost_BST  # Records the previous node as the current node.
    prev = reconstruct_BST_helper(almost_BST.right, inversion_0, inversion_1, prev)
    return prev
# @exclude


def main():
    #      3
    #    2   4
    #  1    5 6
    almost_BST = BinaryTreeNode(3)
    almost_BST.left = BinaryTreeNode(2)
    almost_BST.left.left = BinaryTreeNode(1)
    almost_BST.right = BinaryTreeNode(4)
    almost_BST.right.left = BinaryTreeNode(5)
    almost_BST.right.right = BinaryTreeNode(6)
    reconstruct_BST(almost_BST)
    result = generate_inorder(almost_BST)
    print(*result)
    assert all(result[i] <= result[i+1] for i in range(len(result) - 1))


if __name__ == '__main__':
    main()
