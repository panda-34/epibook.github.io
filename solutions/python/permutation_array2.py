# Permutation_array2.h 98875343ac034c2bd2141da5f5c9c7e25c192d76

# @include
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Traverses the cycle to see if i is the minimum element.
        is_min = True
        j = perm[i]
        while j != i:
            if j < i:
                is_min = False
                break
            j = perm[j]

        if is_min:
            a = i
            temp = A[i]
            while True:
                next_a = perm[a]
                next_temp = A[next_a]
                A[next_a] = temp
                a = next_a
                temp = next_temp
                if a == i:
                    break
# @exclude
