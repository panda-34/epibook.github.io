# Power_set_alternative.cpp 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random
import itertools


# @include
def generate_power_set(input_set):
    power_set = []
    directed_power_set(input_set, 0, [], power_set)
    return power_set


# Generate all subsets whose intersection with input_set[0], ..., input_set[to_be_selected - 1] is exactly selected_so_far.
def directed_power_set(input_set, to_be_selected, selected_so_far, power_set):
    if to_be_selected == len(input_set):
        power_set.append(list(selected_so_far))
        return

    # Generate all subsets that contain input_set[to_be_selected].
    selected_so_far.append(input_set[to_be_selected])
    directed_power_set(input_set, to_be_selected + 1, selected_so_far,
                       power_set)
    selected_so_far.pop()
    directed_power_set(input_set, to_be_selected + 1, selected_so_far,
                       power_set)


# @exclude


# Pythonic solution
def generate_power_set_pythonic(S):
    return [
        list(a)
        for a in itertools.chain.from_iterable(
            itertools.combinations(S, r) for r in range(len(S) + 1))
    ]


def small_test():
    assert sorted(generate_power_set([0, 1, 2])) == [
        [], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]
    ] == sorted(generate_power_set_pythonic([0, 1, 2]))


def main():
    small_test()
    if len(sys.argv) >= 2:
        S = [int(i) for i in sys.argv[1:]]
    else:
        S = list(range(random.randint(1, 10)))
    assert sorted(generate_power_set(S)) == sorted(
        generate_power_set_pythonic(S))


if __name__ == '__main__':
    main()
