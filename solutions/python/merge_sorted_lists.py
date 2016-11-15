# Merge_sorted_lists.h 98875343ac034c2bd2141da5f5c9c7e25c192d76
# Merge_sorted_lists.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
from linked_list_prototype import ListNode


# @include
def merge_two_sorted_lists(L1, L2):
    # Creates a placeholder for the result.
    dummy_head = ListNode()
    tail = dummy_head

    lists = [L1, L2]
    while all(lists):
        cand = min(range(len(lists)), key=lambda i: lists[i].data)
        tail.next = lists[cand]
        tail = tail.next
        lists[cand] = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = lists[0] if lists[0] else lists[1]
    return dummy_head.next


# @exclude


def simple_test():
    L1, L2 = None, None
    assert merge_two_sorted_lists(L1, L2) is None

    L1 = ListNode(123)
    result = merge_two_sorted_lists(L1, L2)
    assert result.data == 123 and result.next is None

    L2 = ListNode(123)
    L1 = None
    result = merge_two_sorted_lists(L1, L2)
    assert result.data == 123 and result.next is None

    L1 = ListNode(-123)
    L2 = ListNode(123)
    result = merge_two_sorted_lists(L1, L2)
    assert result.data == -123 and result.next.data == 123 and result.next.next is None


def main():
    simple_test()
    for _ in range(10000):
        F = None
        L = None
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            m = int(sys.argv[2])
        elif len(sys.argv) == 2:
            n = int(sys.argv[1])
            m = int(sys.argv[1])
        else:
            n = random.randint(0, 99)
            m = random.randint(0, 99)
        for i in range(n, 0, -1):
            temp = ListNode(i, None)
            temp.next = F
            F = temp
        for j in range(m, 0, -1):
            temp = ListNode(j, None)
            temp.next = L
            L = temp

        sorted_head = merge_two_sorted_lists(F, L)
        count = 0
        pre = float('-inf')
        while sorted_head:
            assert pre <= sorted_head.data
            pre = sorted_head.data
            sorted_head = sorted_head.next
            count += 1
        # Make sure the merged list have the same number of nodes as F and L.
        assert count == n + m


if __name__ == '__main__':
    main()
