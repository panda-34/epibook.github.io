# remove-duplicates-sorted-list.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
from linked_list_prototype import ListNode


# @include
def remove_duplicates(L):
    it = L
    while it:
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L
# @exclude


def main():
    L = ListNode(
        2, ListNode(
            2, ListNode(
                2, ListNode(
                    2, ListNode(
                        2, None)))))
    pre = None
    result = remove_duplicates(L)
    count = 0
    while result:
        count += 1
        if pre:
            assert pre.data != result.data
        print(result.data)
        pre = result
        result = result.next
    assert count == 1


if __name__ == '__main__':
    main()
