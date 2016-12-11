# Longest_nondecreasing_subsequence_n2.h bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
# @include
def longest_nondecreasing_subsequence_length(A):
    # max_length[i] holds the length of the longest nondecreasing subsequence
    # of A[0 : i].
    max_length = [1] * len(A)
    for i in range(1, len(A)):
        max_length[i] = max(1 + max(max_length[j] for j in range(i)
                                    if A[i] >= A[j]), max_length[i])
    return max(max_length)


# @exclude
