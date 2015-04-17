# populating-next-right-pointers.cc b4b3a70d8ab942579f85b4416f980d05831af969
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, nxt=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = nxt  # Populates this field.


# @include
def construct_right_sibling(tree):
    left_start = tree
    while left_start:
        populate_children_next_field(left_start)
        left_start = left_start.left


def populate_children_next_field(start_node):
    it = start_node
    while it and it.left:
        it.left.next = it.right
        if it.next:
            it.right.next = it.next.left
        it = it.next
# @exclude


def main():
    #      3
    #    2   5
    #  1  7 4 6
    root = BinaryTreeNode(3)
    root.left = BinaryTreeNode(2)
    root.left.right = BinaryTreeNode(7)
    root.left.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(4)
    root.right.right = BinaryTreeNode(6)
    construct_right_sibling(root)
    assert root.next is None
    assert root.left.next is root.right
    assert root.left.left.next is root.left.right
    assert root.left.right.next is root.right.left
    assert root.right.left.next is root.right.right


if __name__ == '__main__':
    main()
