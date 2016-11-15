# Search_postings_list_recursive.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import itertools
from postings_list_prototype import ListNode


# @include
def search_postings_list(L):
    search_postings_list_helper(L, itertools.count())


def search_postings_list_helper(L, order):
    if L and L.order == -1:
        L.order = next(order)
        search_postings_list_helper(L.jump, order)
        search_postings_list_helper(L.next, order)


# @exclude


def main():
    L = curr = None
    # Build a linked list L->1->2->3->4->5->None.
    for i in range(5):
        temp = ListNode(-1, None, None)
        if curr:
            curr.next = temp
            curr = temp
        else:
            curr = L = temp

    L.jump = None  # no jump from 1
    L.next.jump = L.next.next.next  # 2's jump points to 4
    L.next.next.jump = L  # 3's jump points to 1
    L.next.next.next.jump = None  # no jump from 4
    L.next.next.next.next.jump = L.next.next.next.next  # 5's jump points to 5
    temp = L
    search_postings_list(L)
    # output the jump-first order, should be 0, 1, 4, 2, 3
    assert temp.order == 0
    temp = temp.next
    assert temp.order == 1
    temp = temp.next
    assert temp.order == 4
    temp = temp.next
    assert temp.order == 2
    temp = temp.next
    assert temp.order == 3


if __name__ == '__main__':
    main()
