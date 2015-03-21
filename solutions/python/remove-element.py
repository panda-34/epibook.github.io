# remove-element.cc 848813e190b1b85a8e75107fe8513c3be38ad1a9
import sys
import random


# @include
def remove_element(k, A):
    write_idx = 0
    for i in A:
        if i != k:
            A[write_idx] = i
            write_idx += 1
    return write_idx
# @exclude


def check_ans(A, n, k):
    for i in range(n):
        assert A[i] != k


def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = random.randint(0, 10000)

    for _ in range(1000):
        A = [random.randint(-1000, 1000) for i in range(n)]
        copy_A = A.copy()
        target = random.randint(-1000, 1000)
        size = remove_element(target, A)
        print('size =', size, 'k =', target)
        check_ans(A, size, target)
        copy_A = [x for x in copy_A if x != target]
        print(len(copy_A))
        assert size == len(copy_A)


if __name__ == '__main__':
    main()
