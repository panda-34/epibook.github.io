# Even_odd_merge_linked_list.cpp 98875343ac034c2bd2141da5f5c9c7e25c192d76
import sys
import random
from linked_list_prototype import ListNode


# @include
def even_odd_merge(L):
    if not L:
        return L

    even_list_head = L
    even_list_iter = even_list_head
    predecessor_even_list_iter = None
    odd_list_head = L.next
    odd_list_iter = odd_list_head

    while even_list_iter and odd_list_iter:
        even_list_iter.next = odd_list_iter.next
        predecessor_even_list_iter = even_list_iter
        even_list_iter = even_list_iter.next
        if even_list_iter:
            odd_list_iter.next = even_list_iter.next
            odd_list_iter = odd_list_iter.next

    # Appends odd list to the tail of even list.
    if even_list_iter:
        even_list_iter.next = odd_list_head
    else:
        predecessor_even_list_iter.next = odd_list_head
    return even_list_head
# @exclude


def main():
    head = None
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 1000)
    for i in range(n - 1, -1, -1):
        curr = ListNode(i, None)
        curr.next = head
        head = curr
    ans = even_odd_merge(head)
    x = 0
    count = 0
    while ans:
        count += 1
        assert x == ans.data
        x += 2
        if x >= n:
            x = 1
        print(ans.data)
        ans = ans.next
    assert count == n


if __name__ == '__main__':
    main()
