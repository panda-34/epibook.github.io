# Search_majority.cc bd9b3e8c6bc4755e176bbf01d16d2a77b2bf5147
import sys
import random
import string


# @include
def majority_search(input_stream):
    candidate = ''
    candidate_count = 0
    for it in input_stream:
        if candidate_count == 0:
            candidate = it
            candidate_count = 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate
# @exclude


def rand_string(length):
    ret = (random.choice(string.ascii_lowercase) for i in range(length))
    return ''.join(ret)


def check_ans(stream, ans):
    stream.sort()
    candidate_count = 1
    find = False
    for i in range(1, len(stream)):
        if stream[i] != stream[i - 1]:
            if candidate_count * 2 >= len(stream):
                assert ans == stream[i - 1]
                find = True
            candidate_count = 1
        else:
            candidate_count += 1
    if candidate_count * 2 >= len(stream):
        assert ans == stream[-1]
        find = True
    assert find == True


def main():
    for times in range(10000):
        if len(sys.argv) == 2:
            n = int(sys.argv[1])
        else:
            n = random.randint(1, 1000)
        stream = [rand_string(random.randint(1, 5)) for i in range(n)]
        # generate the majority
        for i in range(n):
            stream.append(stream[-1])
        input_stream = iter(stream)
        ret = majority_search(input_stream)
        print(ret)
        check_ans(stream, ret)


if __name__ == '__main__':
    main()
