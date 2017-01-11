import itertools
import math
import sys
import random


# @include
def buy_and_sell_stock_twice(prices):
    max_total_profit = 0.0
    first_buy_sell_profits = [0] * len(prices)
    min_price_so_far = float('inf')
    # Forward phase. For each day, we record maximum profit if we sell on that day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase. For each day, find the maximum profit if we mak ethe second buy on that day.
    max_price_so_far = float('-inf')
    for i in range(len(prices) - 1, 0, -1):
        max_price_so_far = max(max_price_so_far, prices[i])
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - prices[i] + first_buy_sell_profits[i - 1])
    return max_total_profit


# @exclude
"""O(n^4) checking answer."""


def check_ans(A):
    cap = max(0,
              max([A[i] - A[j] for i in range(1, len(A)) for j in range(i)] or
                  [0]))
    return max(cap,
               max([
                   A[d] - A[c] + A[b] - A[a]
                   for a, b, c, d in itertools.combinations(range(len(A)), 4)
               ] or [0]))


def main():
    for _ in range(1000):
        n = int(sys.argv[1]) if len(sys.argv) == 2 else random.randint(1, 100)
        a = [random.uniform(0, 10000) for i in range(n)]
        assert math.isclose(check_ans(a), buy_and_sell_stock_twice(a))


if __name__ == '__main__':
    main()
