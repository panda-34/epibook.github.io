# Remove_kth_last_list.cpp 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    while k:
        first = first.next
        k -= 1

    second = dummy_head
    while first:
        second = second.next
        first = first.next
    # second points to the (k + 1)-th last node, deletes its successor.
    second.next = second.next.next
    return dummy_head.next
# @exclude


def main():
    L = ListNode(
        1, ListNode(
            2, ListNode(
                3, None)))
    L = remove_kth_last(L, 2)
    assert L.data == 1 and L.next.data == 3
    L = remove_kth_last(L, 2)
    assert L.data == 3 and L.next == None


if __name__ == '__main__':
    main()
