# Linked_list_prototype.h 848813e190b1b85a8e75107fe8513c3be38ad1a9
# @include
class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
# @exclude
    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class DListNode:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def begin(self):
        return self._head

    def end(self):
        return self._tail

    def front(self):
        if not self._head:
            raise ValueError('List is empty')
        return self._head.data

    def back(self):
        if not self._tail:
            raise ValueError('List is empty')
        return self._tail.data

    def emplace_front(self, value):
        node = DListNode(value)
        node.next = self._head
        if self._head:
            self._head.prev = node
        else:
            self._tail = node
        self._head = node
        self._size += 1

    def emplace_back(self, value):
        node = DListNode(value)
        node.prev = self._tail
        if self._tail:
            self._tail.next = node
        else:
            self._head = node
        self._tail = node
        self._size += 1

    def pop_back(self):
        node = self._tail
        if node:
            self._tail = node.prev
            node.prev = None
            if self._tail:
                self._tail.next = None
            else:
                self._head = None
            self._size -= 1
        else:
            raise ValueError('List is empty')

    def erase(self, node):
        if not isinstance(node, DListNode):
            raise ValueError('Invalid node')
        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next
        node.next = node.prev = None
        self._size -= 1
