# insertion-sort-list.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
def insertion_sort(L):
    dummy_head = ListNode(0, L)
    it = L
    while it and it.next:
        if it.data > it.next.data:
            target = it.next
            pre = dummy_head
            while pre.next.data < target.data:
                pre = pre.next
            temp = pre.next
            pre.next = target
            it.next = target.next
            target.next = temp
        else:
            it = it.next
    return dummy_head.next
# @exclude


def main():
    L = ListNode(
        1, ListNode(
            4, ListNode(
                3, ListNode(
                    2, ListNode(
                        5, None)))))
    result = insertion_sort(L)
    pre = None
    while result:
        assert not pre or pre.data <= result.data
        pre = result
        print(result.data)
        result = result.next


if __name__ == '__main__':
    main()
