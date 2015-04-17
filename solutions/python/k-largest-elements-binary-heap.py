# k-largest-elements-binary-heap.cc b4b3a70d8ab942579f85b4416f980d05831af969
import heapq


# @include
def k_largest_in_binary_heap(A, k):
    if k <= 0:
        return []

    # Stores the (-value, index)-pair in candidate_max_heap. This heap is
    # ordered by value field.
    # value is negative to make max_heap instead of python's min_heap
    candidate_max_heap = []
    # The largest element in A is at index 0.
    candidate_max_heap.append((-A[0], 0))
    result = []
    for i in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[left_child_idx], left_child_idx))
        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(candidate_max_heap, (-A[right_child_idx], right_child_idx))
    return result
# @exclude


def main():
    max_heap = [10, 2, 9, 2, 2, 8, 8, 2, 2, 2, 2, 7, 7, 7, 7]
    result = k_largest_in_binary_heap(max_heap, 3)
    expected_result = [10, 9, 8]
    assert result == expected_result
    result = k_largest_in_binary_heap(max_heap, 5)
    expected_result = [10, 9, 8, 8, 7]
    assert result == expected_result

    max_heap = [97, 84, 93, 83, 81, 90, 79, 83, 55, 42, 21, 73]
    result = k_largest_in_binary_heap(max_heap, 3)
    expected_result = [97, 93, 90]
    assert result == expected_result


if __name__ == '__main__':
    main()
