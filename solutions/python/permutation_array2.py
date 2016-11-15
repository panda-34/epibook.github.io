# Permutation_array2.h 98875343ac034c2bd2141da5f5c9c7e25c192d76


# @include
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Traverses the cycle to see if i is the minimum element.
        j = perm[i]
        while j != i:
            if j < i:
                break
            j = perm[j]
        else:
            cyclic_permutation(i, perm, A)


def cyclic_permutation(start, perm, A):
    i, temp = start, A[start]
    while True:
        next_i = perm[i]
        next_temp = A[next_i]
        A[next_i] = temp
        i, temp = next_i, next_temp
        if i == start:
            break
# @exclude
