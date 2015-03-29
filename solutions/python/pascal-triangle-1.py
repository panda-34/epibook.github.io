# pascal-triangle-1.cc 98875343ac034c2bd2141da5f5c9c7e25c192d76
import sys
import random


# @include
def generate_pascal_triangle(n):
    result = []
    for i in range(n):
        curr_row = [1] * (i + 1)
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            curr_row[j] = result[-1][j - 1] + result[-1][j]
        result.append(curr_row)
    return result
# @exclude


def main():
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
