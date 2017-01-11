# Score_combination.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random


# @include
def num_combinations_for_final_score(final_score, individual_play_scores):
    # One way to reach 0.
    num_combinations_for_score = [[0] * (final_score + 1) for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        num_combinations_for_score[i][0] = 1  # One way to reach 0.
        for j in range(1, final_score + 1):
            without_this_play = num_combinations_for_score[i - 1][j] if i >= 1 else 0
            with_this_play = (num_combinations_for_score[i][j - individual_play_scores[i]]
                              if j >= individual_play_scores[i]
                              else 0)
            num_combinations_for_score[i][j] = without_this_play + with_this_play
    return num_combinations_for_score[-1][-1]
# @exclude


def simple_test():
    individual_play_scores = [2, 3, 7]
    assert 4 == num_combinations_for_final_score(12, individual_play_scores)
    assert 1 == num_combinations_for_final_score(5, individual_play_scores)
    assert 3 == num_combinations_for_final_score(9, individual_play_scores)


def check_answer(total_score, score_ways):
    combinations = [0] * (total_score + 1)
    combinations[0] = 1  # One way to reach 0.
    for score in score_ways:
        for j in range(score, total_score + 1):
            combinations[j] += combinations[j - score]
    return combinations[total_score]


def main():
    simple_test()
    individual_play_scores = []
    if len(sys.argv) == 1:
        k = random.randrange(1000)
        individual_play_scores = [random.randint(1, 1000) for _ in range(random.randint(1, 50))]
    elif len(sys.argv) == 2:
        k = int(sys.argv[1])
        individual_play_scores = [random.randint(1, 1000) for _ in range(random.randint(1, 50))]
    else:
        k = int(sys.argv[1])
        individual_play_scores = [int(i) for i in sys.argv[2:]]
    print(num_combinations_for_final_score(k, individual_play_scores))
    assert (num_combinations_for_final_score(k, individual_play_scores) ==
            check_answer(k, individual_play_scores))


if __name__ == '__main__':
    main()
