# tower_hanoi.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


num_steps = 0
# @include
k_num_pegs = 3


def compute_tower_hanoi(num_rings):
    pegs = [[] for i in range(k_num_pegs)]
    # Initialize pegs.
    for i in range(num_rings, 0, -1):
        pegs[0].append(i)

    compute_tower_hanoi_steps(num_rings, pegs, 0, 1, 2)


def compute_tower_hanoi_steps(num_rings_to_move, pegs, from_peg, to_peg, use_peg):
    # @exclude
    global num_steps
    # @include
    if num_rings_to_move > 0:
        compute_tower_hanoi_steps(num_rings_to_move - 1, pegs, from_peg, use_peg, to_peg)
        pegs[to_peg].append(pegs[from_peg].pop())
        print('Move from peg', from_peg, 'to peg', to_peg)
        # @exclude
        num_steps += 1
        # @include
        compute_tower_hanoi_steps(num_rings_to_move - 1, pegs, use_peg, to_peg, from_peg)
# @exclude


def main():
    global num_steps
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10)
    print('n =', n)
    compute_tower_hanoi(n)

    num_steps = 0
    compute_tower_hanoi(4)
    assert 15 == num_steps

    num_steps = 0
    compute_tower_hanoi(1)
    assert 1 == num_steps

    num_steps = 0
    compute_tower_hanoi(0)
    assert 0 == num_steps

    num_steps = 0
    compute_tower_hanoi(10)
    assert 1023 == num_steps


if __name__ == '__main__':
    main()
