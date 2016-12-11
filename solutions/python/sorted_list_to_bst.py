# Sorted_list_to_BST.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from linked_list_prototype import ListNode


# @include
# Returns the root of the corresponding BST. The prev and next fields of the
# list nodes are used as the BST nodes left and right fields, respectively.
# The length of the list is given.
def build_BST_from_sorted_doubly_list(L, n):
    return Build_BST_from_sorted_doubly_list_helper(L, 0, n)[0]


# Builds a BST from the (start + 1)-th to the end-th node, inclusive, in L,
# and returns the root.
def Build_BST_from_sorted_doubly_list_helper(L, start, end):
    if start >= end:
        return None, L

    mid = start + ((end - start) // 2)
    left, L = Build_BST_from_sorted_doubly_list_helper(L, start, mid)
    # The last function call sets L to the successor of the maximum node in
    # the tree rooted at left.
    curr = L
    L = L.next
    curr.prev = left
    curr.next, L = Build_BST_from_sorted_doubly_list_helper(L, mid + 1, end)
    return curr, L


# @exclude


def inorder_traversal(node, pre, depth):
    if node:
        inorder_traversal(node.prev, pre, depth + 1)
        assert pre <= node.data
        print(node.data, '; depth =', depth)
        inorder_traversal(node.next, node.data, depth + 1)


def main():
    tail = None
    length = 0
    for i in reversed(range(4)):
        node = ListNode(i, tail)
        if tail:
            tail.prev = node
        tail = node
        length += 1

    tree = build_BST_from_sorted_doubly_list(tail, length)
    inorder_traversal(tree, -1, 0)


if __name__ == '__main__':
    main()
