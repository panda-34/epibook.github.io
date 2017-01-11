from binary_tree_prototype import BinaryTreeNode


# @include
class BinarySearchTree:
    def __init__(self):
        self._root = None

    # @exclude
    def empty(self):
        return self._root is None

    # @include
    def insert(self, key):
        if self.empty():
            self._root = BinaryTreeNode(key)
        else:
            parent = None
            curr = self._root
            while curr:
                parent = curr
                if key == curr.data:
                    return False  # key already present, no duplicates to be added.
                elif key < curr.data:
                    curr = curr.left
                else:  # key > curr.data.
                    curr = curr.right

            # Inserts key according to key and parent.
            if key < parent.data:
                parent.left = BinaryTreeNode(key)
            else:
                parent.right = BinaryTreeNode(key)
        return True

    def delete(self, key):
        # Find the node with key.
        curr = self._root
        parent = None
        while curr and curr.data != key:
            parent = curr
            curr = curr.left if key < curr.data else curr.right

        if not curr:
            # There's no node with key in this tree.
            return False

        key_node = curr
        if key_node.right:
            # Finds the minimum of the right subtree.
            r_key_node = key_node.right
            r_parent = key_node
            while r_key_node.left:
                r_parent = r_key_node
                r_key_node = r_key_node.left
            # Moves links to erase the node.
            r_key_node.left = key_node.left
            key_node.left = None
            if r_parent.left is r_key_node:
                r_parent.left = r_key_node.right
                r_key_node.right = key_node.right
            key_node.right = None
            self._replace_parent_child_link(parent, key_node, r_key_node)

            # Updates _root link if needed.
            if self._root is key_node:
                self._root = r_key_node
        else:
            # Updates _root link if needed.
            if self._root is key_node:
                self._root = key_node.left
            self._replace_parent_child_link(parent, key_node, key_node.left)
            key_node.left = None
        return True

    # @exclude

    def get_root_val(self):
        return self._root.data

    # @include

    # Replaces the link between parent and child by new_link.
    @staticmethod
    def _replace_parent_child_link(parent, child, new_link):
        if not parent:
            return

        if parent.left is child:
            parent.left = new_link
        else:  # parent.right is child.
            parent.right = new_link


# @exclude


def main():
    BST = BinarySearchTree()
    assert BST.empty() is True
    assert BST.insert(7) is True
    assert BST.insert(8) is True
    assert BST.insert(9) is True
    assert BST.insert(4) is True
    assert BST.insert(3) is True
    assert BST.empty() is False
    assert BST.insert(2) is True
    assert BST.insert(5) is True
    assert BST.delete(7) is True
    assert BST.delete(9) is True
    # should output 8
    assert BST.get_root_val() == 8
    print(BST.get_root_val())
    assert BST.delete(4) is True
    # should output 8
    assert BST.get_root_val() == 8
    print(BST.get_root_val())
    assert BST.delete(8) is True
    # should output 5
    assert BST.get_root_val() == 5
    print(BST.get_root_val())
    assert BST.delete(5) is True
    assert BST.delete(3) is True
    # should output 2
    assert BST.get_root_val() == 2
    print(BST.get_root_val())
    assert BST.delete(2) is True
    assert BST.delete(1) is False
    assert BST.empty() is True
    BST.insert(7)
    assert BST.get_root_val() == 7
    BST.insert(9)
    assert BST.get_root_val() == 7
    BST.delete(7)
    assert BST.get_root_val() == 9


if __name__ == '__main__':
    main()
