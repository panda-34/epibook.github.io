# palindrome-partitioning.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string


# @include
def palindrome_partitioning(input):
    result = []
    partial_partition = []
    directed_palindrome_partitioning(input, 0, partial_partition, result)
    return result


def directed_palindrome_partitioning(input, offset, partial_partition, result):
    if offset == len(input):
        result.append(partial_partition.copy())
        return

    for i in range(offset + 1, len(input) + 1):
        prefix = input[offset : i]
        if is_palindrome(prefix):
            partial_partition.append(prefix)
            directed_palindrome_partitioning(input, i, partial_partition, result)
            del partial_partition[-1]


def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
# @exclude


def check_ans(vecs, input):
    for vec in vecs:
        temp = ''
        for s in vec:
            assert is_palindrome(s)
            temp += s
        assert temp == input


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def simple_test():
    result = palindrome_partitioning('abbbac')
    v0 = ['a', 'b', 'b', 'b', 'a', 'c']
    v1 = ['a', 'b', 'bb', 'a', 'c']
    v2 = ['a', 'bb', 'b', 'a', 'c']
    v3 = ['a', 'bbb', 'a', 'c']
    v4 = ['abbba', 'c']
    golden = [v0, v1, v2, v3, v4]
    assert result == golden


def main():
    simple_test()
    if len(sys.argv) == 2:
        s = sys.argv[1]
        result = palindrome_partitioning(s)
        check_ans(result, s)
        print('string s =', s)
        for vec in result:
            print(*vec)
    else:
        for _ in range(1000):
            s = rand_string(random.randint(0, 10))
            result = palindrome_partitioning(s)
            check_ans(result, s)
            print('string s =', s)
            for vec in result:
                print(*vec)


if __name__ == '__main__':
    main()
