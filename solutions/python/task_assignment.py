# Task_assignment.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import collections
import sys
import random
import itertools

# @include
PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimium_task_assignment(task_durations):
    task_durations.sort()
    optimum_assignments = []
    i, j = 0, len(task_durations) - 1
    while i < j:
        optimum_assignments.append(
            PairedTasks(task_durations[i], task_durations[j]))
        i += 1
        j -= 1
    return optimum_assignments


# @exclude


def optimium_task_assignment_pythonic(task_durations):
    task_durations.sort()
    return [
        PairedTasks(task_1, task_2)
        for task_1, task_2 in itertools.islice(
            zip(task_durations, task_durations[::-1]),
            len(task_durations) // 2)
    ]


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
