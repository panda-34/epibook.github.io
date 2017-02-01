# triangle.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
def minimum_path_weight(triangle):
    result = [0]
    for row in triangle:
        result = [
            row[i] + min(result[max(i - 1, 0)],
                         result[min(i, len(result) - 1)])
            for i in range(len(row))
        ]
    return min(result)


# @exclude

import functools


def minimum_path_weight_pythonic(triangle):
    return min(functools.reduce(lambda res, tri: [r + min(a, b) for r, a, b in zip(
        tri, [float('inf')] + res, res + [float('inf')])], triangle, [0]))


def main():
    A = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    assert 11 == minimum_path_weight(A) == minimum_path_weight_pythonic(A)


if __name__ == '__main__':
    main()
