# Permutation_array1.h 848813e190b1b85a8e75107fe8513c3be38ad1a9

# @include
def apply_permutation(perm, A):
    for i in range(len(A)):
        # Check if the element at index i has already been moved
        # by seeing if perm[i] is negative.
        if perm[i] >= 0:
            a = i
            temp = A[i]
            while True:
                next_a = perm[a]
                next_temp = A[next_a]
                A[next_a] = temp
                # Mark a as visited by using the sign bit. Specifically
                # we subtract len(perm) from each entry in perm.
                perm[a] -= len(perm)
                a = next_a
                temp = next_temp
                if a == i:
                    break

    # Restore perm back.
    for i in range(len(perm)):
        perm[i] += len(perm)
# @exclude
