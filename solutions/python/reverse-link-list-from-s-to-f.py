# reverse-link-list-from-s-to-f.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
def reverse_sublist(L, start, finish):
    if start is finish:
        # No need to reverse since start == finish.
        return L

    dummy_head = ListNode(0, L)
    sublist_head = dummy_head
    k = 1
    while k < start:
        sublist_head = sublist_head.next
        k += 1

    # Reverses sublist.
    sublist_iter = sublist_head.next
    while start < finish:
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
        start += 1
    return dummy_head.next
# @exclude


def main():
    L = ListNode(
        1, ListNode(
            2, ListNode(
                3, None)))
    result = reverse_sublist(L, 3, 3)
    assert (result.data == 1 and result.next.data == 2 and
            result.next.next.data == 3 and not result.next.next.next)
    while result:
        print(result.data)
        result = result.next

    result = reverse_sublist(L, 2, 3)
    assert (result.data == 1 and result.next.data == 3 and
            result.next.next.data == 2 and not result.next.next.next)
    while result:
        print(result.data)
        result = result.next

    L = ListNode(
        3, ListNode(
            5, None))
    result = reverse_sublist(L, 1, 2)
    assert result.data == 5 and result.next.data == 3 and not result.next.next
    while result:
        print(result.data)
        result = result.next


if __name__ == '__main__':
    main()
