# triangle.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
def minimum_path_weight(triangle):
    if not triangle:
        return 0

    # As we iterate, prev_row stores the minimum path sum to each entry in
    # triangle[i - 1].
    prev_row = triangle[0]
    for i in range(1, len(triangle)):
        # Stores the minimum path sum to each entry in triangle[i].
        curr_row = triangle[i].copy()
        curr_row[0] += prev_row[0]  # For the first element.
        for j in range(1, len(curr_row) - 1):
            curr_row[j] += min(prev_row[j - 1], prev_row[j])
        curr_row[-1] += prev_row[-1]  # For the last element.

        prev_row = curr_row
    return min(prev_row)
# @exclude


def main():
    A = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert 11 == minimum_path_weight(A)


if __name__ == '__main__':
    main()
