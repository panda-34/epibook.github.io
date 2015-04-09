# Merge_sorted_lists.h 98875343ac034c2bd2141da5f5c9c7e25c192d76
# Merge_sorted_lists.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
from linked_list_prototype import ListNode


# @include
def merge_two_sorted_lists(F, L):
    # Creates a placeholder for the result.
    dummy_head = ListNode()
    tail = dummy_head

    LF = [L, F]
    while all(LF):
        L_or_F = LF[1].data < LF[0].data
        tail.next = LF[L_or_F]
        tail = tail.next
        LF[L_or_F] = tail.next

    if LF[1]:  # Appends the remaining nodes of F.
        tail.next = LF[1]
    elif LF[0]:  # Appends the remaining nodes of L.
        tail.next = LF[0]
    return dummy_head.next
# @exclude


def main():
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
