# average-top-3-scores.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import operator
import collections
import random
import string
import heapq


# @include
def find_student_with_highest_best_of_three_scores(ifs):
    student_scores = collections.defaultdict(list)
    for line in ifs:
        name, score = line.split()
        score = int(score)
        scores = student_scores[name]
        heapq.heappush(scores, -score)
        if len(scores) > 3:
            heapq.heappop(scores)

    top_student = 'no such student'
    current_top_three_scores_sum = 0
    for name, scores in student_scores.items():
        if len(scores) == 3:
            current_scores_sum = -sum(scores)
            if current_scores_sum > current_top_three_scores_sum:
                current_top_three_scores_sum = current_scores_sum
                top_student = name
    return top_student
# @exclude


def find_student_with_highest_best_of_three_scores_pythionic(ifs):
    student_scores = collections.defaultdict(list)
    for line in ifs:
        name, score = line.split()
        score = int(score)
        scores = student_scores[name]
        if len(scores) < 3:
            heapq.heappush(scores, -score)
        else:
            heapq.heappushpop(scores, -score)

    sum_scores = ((-sum(scores), name) for name, scores in student_scores.items()
                  if len(scores) == 3)
    return max(sum_scores, key=operator.itemgetter(0), default='no such student')[1]


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def simple_test():
    with open('scores.txt', 'w') as ofs:
        ofs.write(
            '''
adnan 100
amit 99
adnan 98
thl 90
adnan 10
amit 100
thl 99
thl 95
adnan 95
''')
    with open('scores.txt') as ifs:
        result = find_student_with_highest_best_of_three_scores(ifs)
    print('result =', result)
    assert result == 'adnan'


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(1, 10000)

    with open('scores.txt', 'w') as ofs:
        for i in range(n):
            test_num = random.randint(0, 20)
            name = rand_string(random.randint(5, 10))
            for _ in range(test_num):
                print(name, random.randint(0, 100), file=ofs)
    with open('scores.txt') as ifs:
        name = find_student_with_highest_best_of_three_scores(ifs)
        ifs.seek(0)
        assert name == find_student_with_highest_best_of_three_scores_pythionic(ifs)
    print('top student is', name)


if __name__ == '__main__':
    main()
