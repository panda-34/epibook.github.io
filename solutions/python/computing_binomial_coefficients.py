# Computing_binomial_coefficients.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def compute_binomial_coefficient(n, k):
    x_choose_y = [[0] * (k + 1) for i in range(n + 1)]
    return compute_x_choose_y(n, k, x_choose_y)

def compute_x_choose_y(x, y, x_choose_y):
    if y == 0 or x == y:
        return 1

    if x_choose_y[x][y] == 0:
        without_y = compute_x_choose_y(x - 1, y, x_choose_y)
        with_y = compute_x_choose_y(x - 1, y - 1, x_choose_y)
        x_choose_y[x][y] = without_y + with_y
    return x_choose_y[x][y]
# @exclude


def compute_binomial_coefficients_space_efficient(n, k):
    k = min(k, n - k)
    table = [0] * (k + 1)
    table[0] = 1  # C(0, 0).
    # C(i, j) = C(i - 1, j) + C(i - 1, j - 1).
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            table[j] = table[j] + table[j - 1]
    return table[k]


def check_ans(n, k):
    number = [n - i for i in range(k)]
    temp = []
    for i in range(2, k + 1):
        find = False
        for a in number:
            if a % i == 0:
                a //= i
                find = True
                break
        if not find:
            temp.append(i)

    res = 1
    for a in number:
        res *= a

    for a in temp:
        res //= a

    return res


def main():
    for times in range(1000):
        if len(sys.argv) == 3:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
        else:
            n = random.randint(1, 21)
            k = random.randint(0, n)

        res = compute_binomial_coefficient(n, k)
        print('res =', res)
        assert res == compute_binomial_coefficients_space_efficient(n, k)
        print(n, 'out of', k, '=', res)
        if len(sys.argv) == 3:
            break


if __name__ == '__main__':
    main()
