# add-two-number-list.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
def add_two_numbers(L1, L2):
    dummy_head = ListNode()
    place_iter = dummy_head
    carry = 0
    while L1 or L2:
        res = carry
        if L1:
            res += L1.data
            L1 = L1.next
        if L2:
            res += L2.data
            L2 = L2.next
        place_iter.next = ListNode(res % 10, None)
        carry = res // 10
        place_iter = place_iter.next
    # carry cannot exceed 1, so we at most need to add one more node.
    if carry:
        place_iter.next = ListNode(carry, None)
    return dummy_head.next
# @exclude


def main():
    L = ListNode(
        2, ListNode(
            4, ListNode(
                3, None)))
    R = ListNode(
        5, ListNode(
            6, ListNode(
                7, None)))
    S = add_two_numbers(L, R)
    assert (S.data == 7 and S.next.data == 0 and S.next.next.data == 1 and
            S.next.next.next.data == 1)
    L = ListNode(
        9, ListNode(
            9, None))
    R = ListNode(9, None)
    S = add_two_numbers(L, R)
    assert S.data == 8 and S.next.data == 0 and S.next.next.data == 1


if __name__ == '__main__':
    main()
