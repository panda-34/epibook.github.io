# LRUCache.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
from linked_list_prototype import LinkedList


# @include
class LRUCache:

    def __init__(self, capacity):
        self._isbn_price_table = {}
        self._lru_queue = LinkedList()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return False, None
        it = self._isbn_price_table[isbn]
        price = it[1]
        # Since key has just been accessed, move it to the front.
        self._move_to_front(isbn, it)
        return True, price

    def insert(self, isbn, price):
        # We add the value for key only if key is not present - we don't update
        # existing values.
        if isbn in self._isbn_price_table:
            # Specification says we should make isbn the most recently used.
            self._move_to_front(isbn, self._isbn_price_table[isbn])
        else:
            if len(self._isbn_price_table) == self._capacity:
                # Removes the least recently used ISBN to get space.
                del self._isbn_price_table[self._lru_queue.back()]
                self._lru_queue.pop_back()
            self._lru_queue.emplace_front(isbn)
            self._isbn_price_table[isbn] = [self._lru_queue.begin(), price]

    def erase(self, isbn):
        if isbn not in self._isbn_price_table:
            return False
        it = self._isbn_price_table[isbn]
        self._lru_queue.erase(it[0])
        del self._isbn_price_table[isbn]
        return True

    # Forces this key-value pair to move to the front.
    def _move_to_front(self, isbn, it):
        self._lru_queue.erase(it[0])
        self._lru_queue.emplace_front(isbn)
        it[0] = self._lru_queue.begin()
# @exclude


def main():
    k_capacity = 2
    c = LRUCache(k_capacity)
    print('c.insert(1, 1)')
    c.insert(1, 1)
    print('c.insert(1, 10)')
    c.insert(1, 10)
    print('c.lookup(2)')
    assert c.lookup(2) == (False, None)
    print('c.lookup(1)')
    assert c.lookup(1) == (True, 1)
    c.erase(1)
    assert c.lookup(1) == (False, None)

    # test capacity constraints honored, also FIFO ordering
    c = LRUCache(k_capacity)
    c.insert(1, 1)
    c.insert(2, 1)
    c.insert(3, 1)
    c.insert(4, 1)
    assert c.lookup(1) == (False, None)
    assert c.lookup(2) == (False, None)
    assert c.lookup(3) == (True, 1)
    assert c.lookup(4) == (True, 1)

    # test retrieval moves to front
    c = LRUCache(k_capacity)
    c.insert(1, 1)
    c.insert(2, 1)
    c.insert(3, 1)
    c.lookup(2)
    c.insert(4, 1)
    assert c.lookup(1) == (False, None)
    assert c.lookup(2) == (True, 1)
    assert c.lookup(3) == (False, None)
    assert c.lookup(4) == (True, 1)

    # test update moves to front
    c = LRUCache(k_capacity)
    c.insert(1, 1)
    c.insert(2, 1)
    c.insert(3, 1)
    c.insert(2, 2)
    c.insert(4, 1)
    assert c.lookup(1) == (False, None)
    assert c.lookup(2) == (True, 1)
    assert c.lookup(3) == (False, None)
    assert c.lookup(4) == (True, 1)

    # test remove
    c = LRUCache(k_capacity)
    c.insert(1, 1)
    c.insert(2, 1)
    c.erase(2)
    c.insert(3, 3)
    assert c.lookup(1) == (True, 1)
    assert c.lookup(2) == (False, None)
    assert c.lookup(3) == (True, 3)


if __name__ == '__main__':
    main()
