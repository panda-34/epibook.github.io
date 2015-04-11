# list-pivoting.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
def list_pivoting(L, x):
    less_head = ListNode()
    equal_head = ListNode()
    greater_head = ListNode()
    less_iter = [less_head]
    equal_iter = [equal_head]
    greater_iter = [greater_head]
    # Populates the three lists.
    it = L
    while it:
        if it.data < x:
            append_to = less_iter
        elif it.data == x:
            append_to = equal_iter
        else:  # it.data > x.
            append_to = greater_iter
        append_to[0].next = it
        append_to[0] = it
        it = it.next
    less_iter[0].next = equal_iter[0].next = greater_iter[0].next = None

    # Combines the three lists.
    if greater_head.next:
        equal_iter[0].next = greater_head.next
    if equal_head.next:
        less_iter[0].next = equal_head.next
    return less_head.next
# @exclude


def main():
    L = ListNode(
        1, ListNode(
            4, ListNode(
                3, ListNode(
                    2, ListNode(
                        5, None)))))
    x = 4
    result = list_pivoting(L, x)
    print()
    before_x = True
    while result:
        if result.data >= x:
            before_x = False
        if before_x:
            assert result.data < x
        else:
            assert result.data >= x
        print(result.data)
        result = result.next


if __name__ == '__main__':
    main()
