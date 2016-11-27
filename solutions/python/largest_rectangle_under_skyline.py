# Largest_rectangle_under_skyline.h bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# Largest_rectangle_under_skyline.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


def calculate_largest_rectangle_alternative(heights):
    # Calculate L.
    s = []
    L = []
    for i in range(len(heights)):
        while s and heights[s[-1]] >= heights[i]:
            del s[-1]
        L.append(-1 if not s else s[-1])
        s.append(i)

    # Clear stack for calculating R.
    s.clear()
    R = [None] * len(heights)
    for i in range(len(heights) - 1, -1, -1):
        while s and heights[s[-1]] >= heights[i]:
            del s[-1]
        R[i] = len(heights) if not s else s[-1]
        s.append(i)

    # For each heights[i], find its maximum area include it.
    max_rectangle_area = 0
    for i in range(len(heights)):
        max_rectangle_area = max(max_rectangle_area, heights[i] * (R[i] - L[i] - 1))
    return max_rectangle_area


# @include
def calculate_largest_rectangle(heights):
    pillar_indices = []
    max_rectangle_area = 0
    for i in range(len(heights) + 1):
        if pillar_indices and i < len(heights) and heights[i] == heights[pillar_indices[-1]]:
            # Replace earlier building with same height by current building. This
            # ensures the later buildings have the correct left endpoint.
            pillar_indices[-1] = i
        # By iterating to len(heights) instead of len(heights) - 1, we can
        # uniformly handle the computation for rectangle area here.
        while pillar_indices and is_new_pillar_or_reach_end(heights, i, pillar_indices[-1]):
            height = heights[pillar_indices.pop()]
            width = i if not pillar_indices else i - pillar_indices[-1] - 1
            max_rectangle_area = max(max_rectangle_area, height * width)
        pillar_indices.append(i)
    return max_rectangle_area


def is_new_pillar_or_reach_end(heights, curr_idx, last_pillar_idx):
    return heights[curr_idx] < heights[last_pillar_idx] if curr_idx < len(heights) else True
# @exclude


# O(n^2) implementation checks answer.
def check_answer(A):
    max = -1
    for i in range(len(A)):
        left = i - 1
        right = i + 1
        while left >= 0 and A[left] >= A[i]:
            left -= 1
        while right < len(A) and A[right] >= A[i]:
            right += 1
        area = (right - left - 1) * A[i]
        if area > max:
            max = area
    print(max)
    return max


def small_test():
    A = (2, 3, 4, 1, 2)
    area = calculate_largest_rectangle(A)
    alter_area = calculate_largest_rectangle_alternative(A)
    assert area == alter_area
    assert check_answer(A) == area
    assert 6 == area
    A = (2, 2, 2)
    assert 6 == calculate_largest_rectangle(A)
    A = (1, 1, 2)
    assert 3 == calculate_largest_rectangle(A)


def main():
    small_test()
    for times in range(3000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 1000)
        A = [random.randrange(1000) for i in range(n)]
        area = calculate_largest_rectangle(A)
        alter_area = calculate_largest_rectangle_alternative(A)
        print(area, alter_area)
        assert area == alter_area
        assert check_answer(A) == area


if __name__ == '__main__':
    main()
