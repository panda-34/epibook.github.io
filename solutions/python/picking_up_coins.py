# Picking_up_coins.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import itertools


# @include
def maximum_revenue(coins):
    maximum_revenue_for_range = [[0] * len(coins) for c in coins]
    return compute_maximum_revenue_for_range(coins, 0, len(coins) - 1, maximum_revenue_for_range)


def compute_maximum_revenue_for_range(coins, a, b, maximum_revenue_for_range):
    if a > b:
        # No coins left.
        return 0

    if maximum_revenue_for_range[a][b] == 0:
        max_revenue_a = coins[a] + min(
            compute_maximum_revenue_for_range(coins, a + 2, b, maximum_revenue_for_range),
            compute_maximum_revenue_for_range(coins, a + 1, b - 1, maximum_revenue_for_range))
        max_revenue_b = coins[b] + min(
            compute_maximum_revenue_for_range(coins, a + 1, b - 1, maximum_revenue_for_range),
            compute_maximum_revenue_for_range(coins, a, b - 2, maximum_revenue_for_range))
        maximum_revenue_for_range[a][b] = max(max_revenue_a, max_revenue_b)
    return maximum_revenue_for_range[a][b]
# @exclude


def maximum_revenue_alternative_helper(coins, a, b, prefix_sum, maximum_revenue_for_range):
    if a > b:
        return 0
    elif a == b:
        return coins[a]

    if maximum_revenue_for_range[a][b] == -1:
        maximum_revenue_for_range[a][b] = max(
            coins[a] + prefix_sum[b] - (prefix_sum[a] if a + 1 > 0 else 0) -
            maximum_revenue_alternative_helper(
                coins, a + 1, b, prefix_sum, maximum_revenue_for_range),
            coins[b] + prefix_sum[b - 1] - (prefix_sum[a - 1] if a > 0 else 0) -
            maximum_revenue_alternative_helper(
                coins, a, b - 1, prefix_sum, maximum_revenue_for_range))
    return maximum_revenue_for_range[a][b]


def maximum_revenue_alternative(coins):
    prefix_sum = list(itertools.accumulate(coins))
    maximum_revenue_for_range = [[-1] * len(coins) for c in coins]
    return maximum_revenue_alternative_helper(
        coins, 0, len(coins) - 1, prefix_sum, maximum_revenue_for_range)


def greedy_helper(coins, start, end):
    if start > end:
        return 0

    if coins[start] > coins[end]:
        gain = coins[start]
        if coins[start + 1] > coins[end]:
            gain += greedy_helper(coins, start + 2, end)
        else:
            gain += greedy_helper(coins, start + 1, end - 1)
    else:
        gain = coins[end]
        if coins[start] > coins[end - 1]:
            gain += greedy_helper(coins, start + 1, end - 1)
        else:
            gain += greedy_helper(coins, start, end - 2)
    return gain


def greedy(coins):
    return greedy_helper(coins, 0, len(coins) - 1)


def simple_test():
    coins = [25, 5,  10, 5,  10, 5,  10, 25,
             1,  25, 1,  25, 1,  25, 5,  10]
    assert 140 == maximum_revenue(coins)
    assert maximum_revenue_alternative(coins) == maximum_revenue(coins)
    assert 120 == greedy(coins)


def main():
    simple_test()


if __name__ == '__main__':
    main()
