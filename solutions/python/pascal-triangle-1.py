# pascal-triangle-1.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
import sys
import random


# @include
def generate_pascal_triangle(n):
    pascal_triangle = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            pascal_triangle[i][j] = pascal_triangle[i - 1][
                j - 1] + pascal_triangle[i - 1][j]
    return pascal_triangle
# @exclude


def small_test():
    result = generate_pascal_triangle(3)
    assert result == [[1], [1, 1], [1, 2, 1]]


def main():
    small_test()
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(0, 10)
    print('n =', n)
    result = generate_pascal_triangle(n)
    for i in result:
        print(*i)


if __name__ == '__main__':
    main()
