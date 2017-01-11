# Levenshtein_distance.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string


# @include
def levenshtein_distance(A, B):
    return compute_distance_between_prefixes(A,
                                             len(A) - 1, B,
                                             len(B) - 1,
                                             [[-1] * len(B) for i in A])


def compute_distance_between_prefixes(A, A_idx, B, B_idx,
                                      distance_between_prefixes):
    if A_idx < 0:
        # A is empty so add all of B's characters.
        return B_idx + 1
    elif B_idx < 0:
        # B is empty so delete all of A's characters.
        return A_idx + 1
    if distance_between_prefixes[A_idx][B_idx] == -1:
        if A[A_idx] == B[B_idx]:
            distance_between_prefixes[A_idx][
                B_idx] = compute_distance_between_prefixes(
                    A, A_idx - 1, B, B_idx - 1, distance_between_prefixes)
        else:
            substitute_last = compute_distance_between_prefixes(
                A, A_idx - 1, B, B_idx - 1, distance_between_prefixes)
            add_last = compute_distance_between_prefixes(
                A, A_idx - 1, B, B_idx, distance_between_prefixes)
            delete_last = compute_distance_between_prefixes(
                A, A_idx, B, B_idx - 1, distance_between_prefixes)
            distance_between_prefixes[A_idx][B_idx] = 1 + min(
                substitute_last, add_last, delete_last)
    return distance_between_prefixes[A_idx][B_idx]


# @exclude


def check_answer(A, B):
    # Try to reduce the space usage.
    if len(A) < len(B):
        A, B = B, A

    # Initialization.
    D = list(range(len(B) + 1))
    for i in range(1, len(A) + 1):
        pre_i_1_j_1 = D[0]  # Stores the value of D[i - 1][j - 1].
        D[0] = i
        for j in range(1, len(B) + 1):
            pre_i_1_j = D[j]  # Stores the value of D[i -1][j].
            D[j] = pre_i_1_j_1 if A[i - 1] == B[j - 1] else 1 + min(
                pre_i_1_j_1, D[j - 1], D[j])
            # Previous D[i - 1][j] will become the next D[i - 1][j - 1].
            pre_i_1_j_1 = pre_i_1_j
    return D[-1]


def rand_string(length):
    return ''.join(
        random.choice(string.ascii_lowercase) for i in range(length))


def main():
    # Wiki example (http:#en.wikipedia.org/wiki/levenshtein_distance)
    A, B = 'k', 'sitt'
    assert 4 == levenshtein_distance(A, B)
    A, B = 'Saturday', 'Sunday'
    assert 3 == levenshtein_distance(A, B)
    A, B = 'kitten', 'sitting'
    assert 3 == levenshtein_distance(A, B)

    if len(sys.argv) == 3:
        A, B = sys.argv[1:]
    else:
        A = rand_string(random.randint(1, 100))
        B = rand_string(random.randint(1, 100))
    print(A)
    print(B)
    print(levenshtein_distance(A, B))
    assert levenshtein_distance(A, B) == check_answer(A, B)


if __name__ == '__main__':
    main()
