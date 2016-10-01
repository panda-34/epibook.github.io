# sort-list.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
from linked_list_prototype import ListNode
from merge_sorted_lists import merge_two_sorted_lists


# @include
def stable_sort_list(L):
    # Base cases: L is empty or a single node, nothing to do.
    if not L or not L.next:
        return L

    # Find the midpoint of L using a slow and a fast pointer.
    pre_slow = None
    slow = fast = L
    while fast and fast.next:
        pre_slow = slow
        fast = fast.next.next
        slow = slow.next
    pre_slow.next = None  # Splits the list into two equal-sized lists.
    return merge_two_sorted_lists(stable_sort_list(L), stable_sort_list(slow))
# @exclude


def main():
    for _ in range(10000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randrange(100)
        L = None
        for i in range(n):
            L = ListNode(random.randrange(100), L)

        sorted_head = stable_sort_list(L)
        count = 0
        pre = float('-inf')
        while sorted_head:
            assert pre <= sorted_head.data
            pre = sorted_head.data
            sorted_head = sorted_head.next
            count += 1
        assert count == n


if __name__ == '__main__':
    main()