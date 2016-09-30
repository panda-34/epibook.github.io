# Task_assignment.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import itertools


# @include
def optimium_task_assignment(task_durations):
    task_durations.sort()
    optimum_assignments = []
    i = 0
    j = len(task_durations) - 1
    while i < j:
        optimum_assignments.append((task_durations[i], task_durations[j]))
        i += 1
        j -= 1
    return optimum_assignments
# @exclude


def optimium_task_assignment_pythonic(task_durations):
    task_durations.sort()
    optimum_assignments = list(itertools.islice(
        zip(task_durations, reversed(task_durations)), len(task_durations) // 2))
    return optimum_assignments


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10000)
    A = [random.randrange(100) for i in range(n)]
    P = optimium_task_assignment(A)
    assert P == optimium_task_assignment_pythonic(A)
    max = float('-inf')
    for p in P:
        if p[0] + p[1] > max:
            max = p[0] + p[1]
    print(max)


if __name__ == '__main__':
    main()
