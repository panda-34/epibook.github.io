# Palindrome_linked_list.cpp b4b3a70d8ab942579f85b4416f980d05831af969
import sys
from linked_list_prototype import ListNode
from reverse_linked_list_iterative import reverse_linked_list


# @include
def is_linked_list_a_palindrome(L):
    if L is None:
        return True

    # Finds the second half of L.
    slow = fast = L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Compares the first half and the reversed second half lists.
    first_half_iter = L
    second_half_iter = reverse_linked_list(slow.next)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter = second_half_iter.next
        first_half_iter = first_half_iter.next
    return True
# @exclude


def print_list(L):
    while L:
        print(L.data, end=' ')
        L = L.next
    print()


def main():
    head = None
    if len(sys.argv) > 2:
        # Input the node's value in reverse order.
        for i in sys.argv[1:]:
            curr = ListNode(int(i), head)
            head = curr
        print('Yes' if is_linked_list_a_palindrome(head) else 'No')
    else:
        # A link list is a palindrome.
        for i in range(6, 0, -1):
            curr = ListNode(1, head)
            head = curr
        assert is_linked_list_a_palindrome(head)
        # Still a palindrome linked list.
        head = None
        for i in range(5, 0, -1):
            curr = ListNode(1, head)
            head = curr
        head.next.next.data = 3
        assert is_linked_list_a_palindrome(head)
        # Not a palindrome linked list.
        head = None
        for i in range(5, 0, -1):
            curr = ListNode(i, head)
            head = curr
        assert not is_linked_list_a_palindrome(head)
        assert is_linked_list_a_palindrome(None)


if __name__ == '__main__':
    main()
