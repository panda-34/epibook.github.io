# Permutation_array1.h 848813e190b1b85a8e75107fe8513c3be38ad1a9


# @include
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has not been moved by checking if perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts perm.size() from an entry in perm to make it negative, which indicates the corresponding move has been performed.
            perm[next] -= len(perm)
            next = temp

    # Restore perm.
    perm[:] = [a + len(perm) for a in perm]
# @exclude
