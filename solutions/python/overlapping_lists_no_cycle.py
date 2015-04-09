# Overlapping_lists_no_cycle.h 98875343ac034c2bd2141da5f5c9c7e25c192d76
# Overlapping_lists_no_cycle.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
from linked_list_prototype import ListNode


# @include
def overlapping_no_cycle_lists(L1, L2):
    L1_len = length(L1)
    L2_len = length(L2)

    if L1_len > L2_len:
        L1, L2 = L2, L1  # L2 is the longer list
    # Advances the longer list to get equal length lists.
    L2 = advance_list_by_k(abs(L1_len - L2_len), L2)

    while L1 and L2 and L1 != L2:
        L1 = L1.next
        L2 = L2.next
    return L1  # None implies there is no overlap between L1 and L2.


def length(L):
    ret = 0
    while L:
        ret += 1
        L = L.next
    return ret


# Advances L by k steps.
def advance_list_by_k(k, L):
    while k:
        k -= 1
        L = L.next
    return L
# @exclude


def main():
    # L1: 1->2->3->null
    L1 = ListNode(
        1, ListNode(
            2, ListNode(
                3, None)))
    L2 = L1.next.next
    assert overlapping_no_cycle_lists(L1, L2).data == 3
    # L2: 4->5->null
    L2 = ListNode(
        4, ListNode(
            5, None))
    assert not overlapping_no_cycle_lists(L1, L2)


if __name__ == '__main__':
    main()
