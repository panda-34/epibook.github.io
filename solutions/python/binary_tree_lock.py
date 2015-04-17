# Binary_tree_lock.cpp b4b3a70d8ab942579f85b4416f980d05831af969
# @include
class BinaryTreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.__locked = False
        self.__num_locked_descendants = 0

    def is_locked(self):
        return self.__locked

    def lock(self):
        if self.__num_locked_descendants > 0 or self.__locked:
            return False

        # Tests if any of ancestors are not locked.
        it = self.parent
        while it:
            if it.__locked:
                return False
            it = it.parent

        # Locks itself and increments its ancestors's lock counts.
        self.__locked = True
        it = self.parent
        while it:
            it.__num_locked_descendants += 1
            it = it.parent
        return True

    def unlock(self):
        if self.__locked:
            # Unlocks itself and decrements its ancestors's lock counts.
            self.__locked = False
            it = self.parent
            while it:
                it.__num_locked_descendants -= 1
                it = it.parent
# @exclude


def main():
    root = BinaryTreeNode()
    root.left = BinaryTreeNode()
    root.left.parent = root
    root.right = BinaryTreeNode()
    root.right.parent = root
    root.left.left = BinaryTreeNode()
    root.left.left.parent = root.left
    root.left.right = BinaryTreeNode()
    root.left.right.parent = root.left
    # Should output False.
    assert not root.is_locked()
    print(root.is_locked())
    assert root.lock()
    # Should output True.
    assert root.is_locked()
    assert not root.left.lock()
    print(root.is_locked())
    root.unlock()
    assert root.left.lock()
    assert not root.lock()
    # Should output False.
    assert not root.is_locked()
    print(root.is_locked())
    assert root.right.lock()
    # Should output True.
    assert root.right.is_locked()
    print(root.right.is_locked())
    root.left.unlock()
    assert not root.lock()
    root.right.unlock()
    assert root.lock()


if __name__ == '__main__':
    main()
